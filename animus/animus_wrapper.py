# -*- coding: utf-8 -*-
# Copyright (c) 2020, Cyberselves Universal Ltd.
# All Rights Reserved


from .login_details import LoginDetails
from enum import Enum
import animus_client as animus
import animus_utils as utils
import logging
import numpy as np
import random
import cv2
import time
from .modalities import Robot_Modality

stopFlag = False

log = utils.create_logger("MyAnimusApp", logging.INFO)
log.info(animus.version())


class Animus_Client:
    def __init__(self):
        self.robot = None
        self.setup()

    def setup(self):
        audio_params = utils.AudioParams(
            Backends=["notinternal"],
            SampleRate=16000,
            Channels=1,
            SizeInFrames=True,
            TransmitRate=30,
        )
        setup_result = animus.setup(audio_params=audio_params, logdir="PythonAnimusBasics", loglatency=True)
        if not setup_result.success:
            log.error("Animus Client - Could not setup Animus SDK, reason: " + setup_result.description)
            return False
        self.setup_motor_dictionary()

    def login(self):
        login_result = animus.login_user(
            LoginDetails.username, LoginDetails.password, False
        )
        if login_result.success:
            log.info("Animus Client - Login Success")
            return True
        else:
            log.info("Animus Client - Login Failed")
            return False

    def get_robots(self):
        get_robots_result = animus.get_robots(True, True, False)
        if not get_robots_result.localSearchError.success:
            log.error(get_robots_result.localSearchError.description)

        if not get_robots_result.remoteSearchError.success:
            log.error(get_robots_result.remoteSearchError.description)

        if len(get_robots_result.robots) == 0:
            log.info("Animus Client - No Robots found")
            animus.close_client_interface()
            return []
        else:
            return get_robots_result.robots

    def choose_robot(self, available_robots, chosen_index):
        chosen_robot_details = available_robots.robots[chosen_index]
        self.robot = animus.Robot(chosen_robot_details)

    def connect_to_robot(self):
        if not self.is_robot_selected():
            return False

        robot_name = self.robot.robot_details.name
        if not self.robot.connect().success:
            print(f"Could not connect with robot {robot_name}")
            animus.close_client_interface()
            return False

        print(f"Animus Client - Successfully connected to robot {robot_name}")
        return True

    def is_robot_selected(self):
        if not self.robot:
            print("Animus Client - No robot selected. You must select a robot first.")
            return False

    def open_modality(self, robot_modality):
        if not self.is_robot_selected():
            return False

        robot_name = self.robot.robot_details.name
        if not self.robot.open_modality(robot_modality):
            log.error(f"Could not open {robot_modality} modality on {robot_name}.")
            return False

        print(
            f"Animus Client - Successfully opened {robot_modality} modality on {robot_name}"
        )

        return True

    def list_available_emotions(self):
        log.info(utils.emotions_list)

        return True

    def list_available_motions(self):
        motion_dictionary = utils.get_motor_dict()

        log.info(motion_dictionary)
        return True

    def dispose_animus(self):
        if self.robot:
            self.robot.disconnect()
        animus.close_client_interface()

    def demo_speech(self, message):
        if not self.is_robot_selected():
            return False

        try:
            robot_name = self.robot.robot_details.name
            message = message or input(f"Hi, I am {robot_name}, nice to meet you!")
            self.robot.set_modality(Robot_Modality.SPEECH, message)
            self.robot.set_modality(
                Robot_Modality.EMOTION, random.choice(utils.emotions_list)
            )
        except KeyboardInterrupt:
            log.info("Animus Client - Demo Speech interrupted")
            return False
        except SystemExit:
            log.info("Animus Client - Demo Speech interrupted")
            return False

        return True

    def setup_motor_dictionary(self):
        motorDict = utils.get_motor_dict()
        list_of_motions = [motorDict.copy()]
        motorDict["head_left_right"] = 2 * utils.HEAD_RIGHT
        motorDict["head_up_down"] = 2 * utils.HEAD_UP
        motorDict["head_roll"] = 0.0
        motorDict["body_forward"] = 0.0
        motorDict["body_sideways"] = 0.0
        motorDict["body_rotate"] = 0.0
        motorDict["head_left_right"] = 2 * utils.HEAD_LEFT
        motorDict["head_up_down"] = 2 * utils.HEAD_DOWN
        list_of_motions.append(motorDict.copy())

        return list_of_motions

    def demo_motion(self, log):
        num_of_received_images = 0
        next_motion_index = 0

        try:
            cv2.namedWindow("Robot View")
            while next_motion_index < 4:
                image_list, response = self.robot.get_modality("vision", True)
                if response.success:
                    cv2.imshow("RobotView", image_list[0].image)
                    delay = cv2.waitKey(1)

                    if delay == 27:
                        break
                    num_of_received_images += 1

                    if num_of_received_images > 100:
                        num_of_received_images = 0

                        if next_motion_index >= len(self.list_of_motions):
                            break

                        self.robot.set_modality(
                            Robot_Modality.MOTOR,
                            list(self.list_of_motions[next_motion_index].values()),
                        )

                        next_motion_index += 1
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
        except SystemExit:
            cv2.destroyAllWindows()

        cv2.destroyAllWindows()
