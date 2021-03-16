import json
import time

import cv2
import eventlet
from models.modalities import Robot_Modality

from woz_utils.proto_converters import convert_animus_response_to_dict

eventlet.monkey_patch()


class Video_Reader:
    def __init__(self, robot=None):
        self.video = None
        self.capture = True
        self.robot = robot

    def start_capture(self):
        if not self.robot: 
            yield None
            raise StopIteration

        try:
            print("capture", str(self.capture))
            while self.capture:
                imageList, response = self.robot.get_modality("vision", True)
                
                print("capturing result", json.dumps(convert_animus_response_to_dict(response)))
                
                if response.success:
                    print("got a frame list, success: " + str(response.success))
                    for image in imageList:
                        ret, jpeg = cv2.imencode(".jpg", image.image)
                        frame = jpeg.tobytes()
                        yield (
                            b"--frame\r\n"
                            b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n"
                        )
                        time.sleep(0)
        except Exception as e:
            print("error getting video", e)

        self.robot.close_modality("vision")
        raise StopIteration


class Mockup_Video_Reader:
    def __init__(self, robot=None):
        self.video = None
        self.capture = True
        self.robot = robot

    def start_capture(self):
        videoReader = cv2.VideoCapture(0)
        while self.capture:
            success, image = videoReader.read()
            if success:
                print("got a frame list, success: " + str(success))
                ret, jpeg = cv2.imencode(".jpg", image)
                frame = jpeg.tobytes()
                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n"
                )
                time.sleep(0)

        videoReader.release()
        raise StopIteration
