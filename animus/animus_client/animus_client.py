# -*- coding: utf-8 -*-
# Copyright (c) 2020, Cyberselves Universal Ltd.
# All Rights Reserved
# Author: Daniel Camilleri <daniel@cyberselves.com>

from typing import Any, Tuple
from lib_client import animus_client_py3 as animus_client
from animus_utils import animus_utils as utils
from models.i_audio_params import Animus_Audio_Params
from models.i_animus_response import Animus_Response, Animus_Robot_Search_Response
import logging
import numpy as np

log = utils.create_logger("AnimusClient", logging.INFO)
_animus_client_version = "v2.1.0"
_animus_client_build = "486"
_animus_core_version = "v2.1.5"
_sdk_version = "v2.0.6"
_sdk_build = "529"
_sdk_build_date = "2021-02-05-22:31:48-UTC"


def version():
    """ #### Returns the version of the animus client and animus core libraries"""

    version_string = animus_client.VersionGo()    
    log.info(version_string)
    return version_string


def setup(audio_params: Animus_Audio_Params, logdir: str, loglatency: bool)-> Animus_Response:
    """ #### Sets required arguments for the animus client

        #### Args:
                `audio_params (utils.AudioParams)`: The parameters for audio transmission / reception. If None passed, default parameters are used: 
                                            backends: [""], 
                                            sampleRate: 16000, 
                                            Channels: 1, 
                                            SizeInFrames: True, 
                                            TransmitRate: 20
        logdir (str): The directory where to store logs
        loglatency (bool): If set to True, introduces a delay to the logs.

    Returns:
        Animus_Response: a dictionary describing the result of the operation 
    """

    if audio_params is None:
        audio_params = utils.AudioParams(
            Backends=[""],
            SampleRate=16000,
            Channels=1,
            SizeInFrames=True,
            TransmitRate=20
        )

    setup_request = utils.SetupClientProto(
        audio_params=audio_params,
        logDir=logdir,
        latencyLogging=loglatency,
    ).SerializeToString()
    return utils.Error().FromString(
        animus_client.Setup(setup_request, len(setup_request))
    )


def login_user(username: str, password: str, system_login: bool) -> Animus_Response:
    """ Method to login with your username and password and initialise communication session """
    
    log.info("Logging in user")

    login_request = utils.LoginProto(
        username=username,
        password=password,
        systrayLogin=system_login
    ).SerializeToString()

    return utils.Error().FromString(
        animus_client.LoginUser(login_request, len(login_request))
    )


def get_robots(get_local: bool, get_remote: bool, get_system: bool) -> Animus_Robot_Search_Response:
    """Method to get the list of robots that are available locally on the local network or remotely"""

    get_robots_request = utils.GetRobotsProtoRequest(
        getLocal=get_local,
        getRemote=get_remote,
        systrayRobot=get_system
    ).SerializeToString()

    return utils.GetRobotsProtoReply().FromString(
        animus_client.GetRobots(get_robots_request, len(get_robots_request))
    )


def close_client_interface() -> None:
    """#### Closes the client interface initialised with the setup method

        `Note:` You MUST dispose of the connected robots correctly first, by calling their "disconnect()" method.
                      Failing to do so may result in temporary robot unavailability because of orphan connections.
    """

    log.info("Animus Session closed")
    animus_client.CloseClientInterfaceGo()


class Robot:
    """ #### This class represents a robot connection. You can have multiple robots connected, 
        #### each with their own class to allow for multiple synchronised robot control
    """

    def __init__(self, robot_details):
        """The constructor accepts the robot details obtained from `get_robots()`"""

        self.robot_details = robot_details
        self.robot_id = self.robot_details.robot_id

    def connect(self) -> Animus_Response:
        """ Starts a peer to peer connection with the robot using the robot details
            previously passed in the constructor.
        """

        log.info("Connecting with robot {}".format(self.robot_details.name))

        connect_request = utils.ChosenRobotProto(
            chosenOne=self.robot_details
        ).SerializeToString()

        return utils.Error().FromString(
            animus_client.Connect(connect_request, len(connect_request))
        )

    def open_modality(self, modality_name: str)-> Animus_Response:
        """ #### Opens a modality channel
            #### Args:
                        `modality_name (str)`: The modality channel
        """
        
        log.info("Opening {} modality".format(modality_name))

        open_modality_request = utils.OpenModalityProto(
            modalityName=modality_name,
            fps=30
        ).SerializeToString()

        return utils.Error().FromString(
            animus_client.OpenModality(self.robot_id.encode(), open_modality_request, len(open_modality_request))
        )
    
    def set_modality(self, modality_name: str, sample)-> Animus_Response:
        """ #### Sends data on a modality channel
            #### Args:
                        `modality_name (str)`: The modality channel
                        `sample (any)`: any data supported by the library (e.g. list, str, etc.)

            `NOTE`:  sample is validated in `validate_encode_data()` before being transmitted
        """

        dtype, data, data_len = utils.encode_data(sample)
        if dtype is not None:
            return utils.Error().FromString(
                animus_client.SetModality(self.robot_id.encode(), modality_name.encode(), dtype, data, data_len)
            )
        else:
            return { 
                "success": False,
                "code": 4,
                "description": f"{type(sample)} data type is unsupported"
            }

    def get_modality(self, modality_name: str, blocking: bool=False)->Tuple[Any, Animus_Response]:
        """ #### Reads data from a modality channel
            #### Args:
                        `modality_name (string)`: The modality channel
                        `blocking (bool)`: Whether this operation should happen synchronously or not
                
            `returns`: an object whose type depends on the data being transmitted on the channel
        """

        get_result = animus_client.GetModality(self.robot_id.encode(), modality_name.encode(), int(bool(blocking)))
        sample = utils.GetModalityProto().FromString(get_result)

        if sample.error.success:
            new_sample = utils.decode_data(sample.sample)
        else:
            new_sample = None
        return new_sample, sample.error


    def close_modality(self, modality_name) -> Animus_Response:
        """ #### Closes a modality channel 
            #### Args:
                        `modality_name (str)`: The modality channel
        """

        log.info("Closing {} modality".format(modality_name))
        return utils.Error().FromString(
            animus_client.CloseModality(self.robot_id.encode(), modality_name.encode())
        )

    def disconnect(self) -> Animus_Response:
        """ #### This method closes the peer to peer connection for the respective robot"""
        
        log.info("Disconnecting from {}".format(self.robot_details.name))
        return utils.Error().FromString(
            animus_client.Disconnect(self.robot_id.encode())
        )
