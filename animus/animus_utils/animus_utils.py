# -*- coding: utf-8 -*-
# Copyright (c) 2020, Cyberselves Universal Ltd.
# All Rights Reserved
# Author: Daniel Camilleri <daniel@cyberselves.com>
import json
import logging
import threading
import time
import types
from collections import namedtuple, OrderedDict
import numpy as np
from functools import partial
import animus_utils.animus_data_pb2 as animus_data
import cv2
import base64

HEAD_RIGHT = -1.0
HEAD_LEFT = 1.0
HEAD_UP = -1.0
HEAD_DOWN = 1.0
BODY_FORWARD = 1.0
BODY_BACKWARD = -1.0
BODY_LEFT = -1.0
BODY_RIGHT = 1.0
BODY_CLOCKWISE = 1.0
BODY_ANTICLOCKWISE = -1.0


def create_logger(name, level):
    logger = logging.getLogger(name)
    if not len(logger.handlers):
        formatter = logging.Formatter('[ %(levelname)-5s - {:10} ] %(asctime)s - %(message)s'.format(name))
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)

        logger.addHandler(ch)
        logger.setLevel(level)

    return logger


log = create_logger("AnimusUtils", logging.INFO)
discover_log = create_logger("DiscoverModalities", logging.INFO)
dummy_log = create_logger("DummyModality", logging.INFO)
encode_log = create_logger("Encoder", logging.INFO)
decode_log = create_logger("Decoder", logging.INFO)

# # Connection struct definitions
emotions_list = ["angry", "fear", "sad", "happy", "surprised", "neutral"]
audio_backends = ["alsa", "wasapi", "dsound", "winmm", "pulse", "jack", "coreaudio",
                  "sndio", "audio4", "oss", "opensl", "openal", "sdl"]


def get_motor_dict():
    ret = OrderedDict()
    ret["head_left_right"] = 0.0
    ret["head_up_down"] = 0.0
    ret["head_roll"] = 0.0
    ret["body_forward"] = 0.0
    ret["body_sideways"] = 0.0
    ret["body_rotate"] = 0.0
    ret["tracking_left_arm"] = -1.0
    ret["tracking_right_arm"] = -1.0
    return ret


class RobotAction:
    def __init__(self):
        self.data = None
        self.modality = None


class PyImageSample:
    def __init__(self, source=None, shape=None, image=None, image_type=None, transform=None, compression=None):
        self.source = source
        self.shape = shape
        self.image = image
        self.image_type = image_type
        self.transform = transform
        self.compression = compression

    def from_proto_image(self, image_sample):
        npimage = np.frombuffer(image_sample.data, np.uint8).reshape([int(image_sample.data_shape[1] * 3 / 2), image_sample.data_shape[0]])
        npimage = cv2.cvtColor(npimage, cv2.COLOR_YUV2BGR_I420)

        self.source = image_sample.source
        self.shape = image_sample.data_shape
        self.image = npimage
        self.image_type = image_sample.image_type
        self.transform = image_sample.transform
        self.compression = image_sample.compression

    def to_proto_image(self):
        return animus_data.ImageSample(
            source=self.source,
            data_shape=self.shape,
            data=self.image.tostring(),
            image_type=self.image_type,
            transform=self.transform,
            compression=self.compression,
        )

    def encode_image(self, image):
        self.shape = [image.shape[1], image.shape[0], image.shape[2]]
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV_I420)


class PyAudioSample:
    def __init__(self, source=None, num_samples=None, sample_rate=None, audio=None, channels=None, transform=None, compression=None):
        self.source = source
        self.num_samples = num_samples
        self.sample_rate = sample_rate
        self.audio = audio
        self.channels = channels
        self.transform = transform
        self.compression = compression

    def from_proto_audio(self, audio_sample):
        self.source = audio_sample.source
        self.num_samples = audio_sample.num_samples
        self.sample_rate = audio_sample.sample_rate
        self.audio = audio_sample.data
        self.channels = audio_sample.channels
        self.transform = audio_sample.transform
        self.compression = audio_sample.compression

    def to_proto_audio(self):
        return animus_data.AudioSample(
            source=self.source,
            data=self.audio.tobytes(),
            num_samples=self.num_samples,
            sample_rate=self.sample_rate,
            channels=self.channels,
            transform=self.transform,
            compression=self.compression,
        )

    def encode_audio(self, audio, sample_rate, channels):
        self.sample_rate = sample_rate
        self.channels = channels
        self.audio = audio.tostring()
        self.num_samples = int(len(audio)/channels)


def decode_data(sample):
    if sample.data_type == animus_data.DataMessage.IMAGE:
        image_samples = animus_data.ImageSamples().FromString(sample.data)
        image_list = []
        for im in image_samples.samples:
            new_pyimage = PyImageSample()
            new_pyimage.from_proto_image(im)
            image_list.append(new_pyimage)
        return image_list

    elif sample.data_type == animus_data.DataMessage.AUDIO:
        audio_samples = animus_data.AudioSamples().FromString(sample.data)
        audio_list = []
        for frame in audio_samples.samples:
            new_pyaudio = PyAudioSample()
            new_pyaudio.from_proto_audio(frame)
            audio_list.append(new_pyaudio)
        return audio_list

    elif sample.data_type == animus_data.DataMessage.STRING:
        return animus_data.StringSample().FromString(sample.data).data

    elif sample.data_type == animus_data.DataMessage.FLOAT32ARR:
        return animus_data.Float32Array().FromString(sample.data).data

    elif sample.data_type == animus_data.DataMessage.INT64ARR:
        return animus_data.Int64Array().FromString(sample.data).data
    else:
        decode_log.info("decoding {} datatype unhandled".format(sample.data_type))
        return None


def encode_data(sample):
    encoded_dtype = None
    encoded_sample = None

    if isinstance(sample, list):
        if isinstance(sample[0], float):
            encoded_sample = animus_data.Float32Array(data=np.asarray(sample, dtype=np.float32)).SerializeToString()
            encoded_dtype = animus_data.DataMessage.FLOAT32ARR

        elif isinstance(sample[0], int):
            encoded_sample = animus_data.Int64Array(data=np.asarray(sample, dtype=np.int64)).SerializeToString()
            encoded_dtype = animus_data.DataMessage.INT64ARR

        elif isinstance(sample[0], PyImageSample):
            image_samples = animus_data.ImageSamples()
            for s in sample:
                image_samples.samples.append(s.to_proto_image())

            encoded_sample = image_samples.SerializeToString()
            encoded_dtype = animus_data.DataMessage.IMAGE

        elif isinstance(sample[0], PyAudioSample):
            audio_samples = animus_data.AudioSamples()
            for s in sample:
                audio_samples.samples.append(s.to_proto_audio())

            encoded_sample = audio_samples.SerializeToString()
            encoded_dtype = animus_data.DataMessage.AUDIO

        else:
            encode_log.error("list of {} data type is unsupported".format(type(sample[0])))
            return None, None, 0
    elif isinstance(sample, PyImageSample):
        image_samples = animus_data.ImageSamples()
        image_samples.samples.append(sample.to_proto_image())

        encoded_sample = image_samples.SerializeToString()
        encoded_dtype = animus_data.DataMessage.IMAGE

    elif isinstance(sample, PyAudioSample):
        audio_samples = animus_data.AudioSamples()
        audio_samples.samples.append(sample.to_proto_audio())

        encoded_sample = audio_samples.SerializeToString()
        encoded_dtype = animus_data.DataMessage.AUDIO

    elif isinstance(sample, str):
        encoded_sample = animus_data.StringSample(data=sample).SerializeToString()
        encoded_dtype = animus_data.DataMessage.STRING

    else:
        encode_log.error("{} data type is unsupported".format(type(sample)))
        return None, None, 0

    return encoded_dtype, encoded_sample, len(encoded_sample)



def discover_modalities(driver_class):
    method_list = [func for func in dir(driver_class) if
                   callable(getattr(driver_class, func)) and not func.startswith("__")]

    init_modalities = [m.replace("_initialise", "") for m in method_list if "_initialise" in m]
    close_modalities = [m.replace("_close", "") for m in method_list if "_close" in m]
    set_modalities = [m.replace("_set", "") for m in method_list if "_set" in m]
    get_modalities = [m.replace("_get", "") for m in method_list if "_get" in m]

    # After getting lists for init close set and get,
    # find modalities that are present in init, close and get or set.
    modalities_dict = OrderedDict()

    input_modalities = []
    output_modalities = []
    for priority, mod in enumerate(init_modalities):
        if mod in close_modalities:
            if mod in set_modalities:
                modalities_dict[mod] = ["input", priority]
                input_modalities.append(mod)
            elif mod in get_modalities:
                modalities_dict[mod] = ["output", priority]
                output_modalities.append(mod)
            else:
                discover_log.warning("{} Modality incomplete. No set or get method".format(mod))
        else:
            discover_log.warning("{} Modality incomplete. No close method".format(mod))

    return input_modalities, output_modalities


class EmptyHelperClass(object):
    def __init__(self):
        pass


class DummyModality(object):
    def __init__(self, name):
        self.name = name

    def open(self):
        dummy_log.error("{} modality is not implemented for this robot. Cannot open()".format(self.name))
        return False

    def get(self):
        dummy_log.error("{} modality is not implemented for this robot. Cannot get()".format(self.name))
        return None

    def set(self):
        dummy_log.error("{} modality is not implemented for this robot. Cannot set()".format(self.name))
        pass

    def close(self):
        dummy_log.error("{} modality is not implemented for this robot. Cannot close()".format(self.name))
        pass


def check_function(func, devmode):
    if not devmode:
        return True

    if isinstance(func, types.MethodType) or isinstance(func, types.FunctionType) or isinstance(func, partial):
        return True
    else:
        return False


class FpsLag:
    def __init__(self, log, modality_name, interval=128):
        self.count = 0
        self.interval = interval
        self.cumulative_lag = 0
        self.fps_startt = time.time()
        self.name = modality_name
        self.log = log
        self.average_fps = 0
        self.average_lag = 0

    def increment(self, send_timestamp=None):
        self.count += 1
        if send_timestamp is not None:
            self.cumulative_lag += time.time() - send_timestamp

        if self.count == self.interval:
            endt = time.time()
            self.average_fps = self.interval / (endt - self.fps_startt)
            if send_timestamp is not None:
                self.average_lag = self.cumulative_lag / self.interval
                self.log.info("{} - {:.2f} fps ------ {:.2f} lag".format(self.name.capitalize(),
                                                                         self.average_fps, self.average_lag))
            else:
                self.log.info("{} - {:.2f} fps ".format(self.name.capitalize(), self.average_fps))

            self.fps_startt = endt
            self.count = 0
            self.cumulative_lag = 0
            return True
        return False


class PeriodicSampler:
    def __init__(self, name, periodic_function, rate, devmode, success_callback=None):
        self._name = name
        self._periodic_function = periodic_function
        self.requested_rate = rate

        if check_function(success_callback, devmode):
            self._success_callback = success_callback
        else:
            raise ValueError("Callback must be a function")

        self._result = None
        self._run_flag = True
        self.log = create_logger(name="Sample Loop".format(self._name), level=logging.INFO)
        self.perf = FpsLag(log=self.log, modality_name=self._name, interval=128)

    def run(self):
        rate_delay = 1.0/self.requested_rate

        self.log.info("Started {} sampling loop".format(self._name))

        average_fps = -1
        while self._run_flag:
            time.sleep(rate_delay)

            self._result = self._periodic_function()

            if self._result is not None:
                self._success_callback(self._result, average_fps)
                if self.perf.increment():
                    rate_delay += 1.0 / self.requested_rate - 1.0 / self.perf.average_fps

                    # samp_log.info("{} - {:.2f} fps".format(self._name.capitalize(), average_fps))

                    if rate_delay < 0:
                        rate_delay = 0

        self.log.info("{} sampling loop stopped".format(self._name.capitalize()))

    @property
    def result(self):
        """
        Returns:
            Result of the function.
        """
        return self._result

    def stop(self):
        self._run_flag = False


