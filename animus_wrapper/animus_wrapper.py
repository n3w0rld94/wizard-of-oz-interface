# author: Ilyasse Fakhreddine
# date: 03/2021
import logging
import random
from typing import Generator, List, Tuple

import animus_client as animus
import animus_utils as utils
import cv2
from models.i_animus_response import Animus_Response
from models.i_login_details import Animus_Login_Details
from models.modalities import Robot_Modality
from woz_utils.proto_converters import convert_animus_response_to_dict
from woz_utils.server_utils import (
    get_failure_response,
    get_failure_response_body,
    get_missing_robot_response_body,
    get_success_response_body,
    get_unopened_modality_response_body,
)
from woz_utils.video_reader import Video_Reader

log = utils.create_logger("WoZ App", logging.INFO)
log.info(animus.version())


class Animus_Client:
    """ A wrapper to the Animus client functionalities """

    def __init__(self, robot: animus.Robot = None) -> animus.Robot:
        self.robot = robot
        self.open_modalities_by_robot_id = {}
        self.setup()

    def set_open_modality(self, modality_name, is_open=False):
        if self.robot:
            robot_id = self.robot.robot_id
            open_modalities = self.open_modalities_by_robot_id.get(robot_id)
            self.open_modalities_by_robot_id[robot_id] = (
                open_modalities if open_modalities else {}
            )
            self.open_modalities_by_robot_id[robot_id][modality_name] = is_open

    def is_modality_open(self, modality_name):
        if self.robot:
            robot_id = self.robot.robot_id
            open_modalities = self.open_modalities_by_robot_id.get(robot_id)
            if open_modalities and open_modalities.get(modality_name):
                return True

        return False

    def setup(self):
        audio_params = utils.AudioParams(
            Backends=["alsa"],
            SampleRate=16000,
            Channels=1,
            SizeInFrames=True,
            TransmitRate=30,
        )
        setup_result = animus.setup(
            audio_params=audio_params, logdir="PythonAnimusBasics", loglatency=True
        )
        if not setup_result.success:
            log.error(
                f"Animus Client - Could not setup Animus SDK, reason: {setup_result.description}"
            )
            return False
        self.setup_motor_dictionary()

    def login(self, username: str, password: str) -> Animus_Response:
        if not username or not password:
            username = Animus_Login_Details.username
            password = Animus_Login_Details.password

        login_result = animus.login_user(
            username, password, system_login=False
        )  # use user and psw provided, System Login if SysTray software installed (not our case)
        if login_result.success:
            log.info("Login Success")
            return convert_animus_response_to_dict(login_result)
        else:
            log.error(f"Login Failed. Reason: {login_result.description}")
            return convert_animus_response_to_dict(login_result)

    def get_robots(
        self, get_local: bool, get_remote: bool, get_system: bool
    ) -> Tuple[List, List[Animus_Response]]:
        get_robots_result = animus.get_robots(get_local, get_remote, get_system)
        errors = []

        if not get_robots_result.localSearchError.success:
            dict_error = convert_animus_response_to_dict(
                get_robots_result.localSearchError
            )
            errors.append(dict_error)

            description = get_robots_result.localSearchError.description
            log.error(f"Local network search failed: {description}")

        if not get_robots_result.remoteSearchError.success:
            dict_error = convert_animus_response_to_dict(
                get_robots_result.localSearchError
            )
            errors.append(dict_error)

            description = get_robots_result.remoteSearchError.description
            log.error(f"Remote search failed: {description}")

        if len(get_robots_result.robots) == 0:
            log.info("Animus Client - No Robots found")
            return [], errors
        else:
            return get_robots_result.robots, errors

    # Parameter passed should looks like so: available_robots.robots[chosen_index]
    ## TODO: Create Class for robot_details
    def choose_robot(self, robot) -> bool:
        if not robot:
            log.warn("No robot selected.")
            return get_missing_robot_response_body()

        try:
            self.robot = animus.Robot(robot)
        except Exception as e:
            log.error("choose_robot: ", e)
            return get_failure_response_body("Unable to choose robot")

        return get_success_response_body("Robot instance created")

    def connect_to_robot(self) -> Animus_Response:
        if not self.is_robot_selected():
            return get_missing_robot_response_body()

        robot_name = self.robot.robot_details.name
        try:
            connection_result = self.robot.connect()

            if not connection_result.success:
                log.warn(
                    f"Could not connect with robot {robot_name}. Reason: {connection_result.description}"
                )

                return convert_animus_response_to_dict(connection_result)

            log.info(f"Successfully connected to robot {robot_name}")
        except Exception as e:
            log.error("connect_to_robot", e)

        return get_success_response_body("Connected")

    def is_robot_selected(self):
        if not self.robot:
            log.warn("No robot selected.")
            return False

        return True

    def open_modality(self, modality_name):
        """#### Opens a modality channel
        #### Args:
                    `modality_name (str)`: The modality channel
        """

        if not self.is_robot_selected():
            return False
        if self.is_modality_open(modality_name):
            return True

        robot_name = self.robot.robot_details.name
        open_modality_result = self.robot.open_modality(modality_name)

        if not open_modality_result:
            description = open_modality_result.description
            log.error(
                f"Could not open {modality_name} modality on {robot_name}. Reason: {description}"
            )

            return False

        self.set_open_modality(modality_name, True)
        log.info(f"Successfully opened {modality_name} modality on {robot_name}")

        return True

    def close_modality(self, modality_name):
        """#### Opens a modality channel
        #### Args:
                    `modality_name (str)`: The modality channel
        """

        if not self.is_robot_selected():
            return False
        if not self.is_modality_open(modality_name):
            return True

        close_modality_result = self.robot.close_modality(modality_name)
        if not close_modality_result:
            robot_name = self.robot.robot_details.name
            description = close_modality_result.description
            log.error(
                f"Could not close {modality_name} modality on {robot_name}. Reason: {description}"
            )
            return False

        self.set_open_modality(modality_name, False)
        return True

    def list_available_emotions(self):
        log.info(utils.emotions_list)

        return True

    def list_available_motions(self) -> None:
        motion_dictionary = utils.get_motor_dict()
        motion_list = list(motion_dictionary.keys)

        log.info("------ List of built-in motions ---- ")
        log.info(motion_list)

    def dispose_animus(self):
        if self.robot:
            self.robot.disconnect()
        animus.close_client_interface()

    def demo_speech(self, message: str) -> bool:
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

    def setup_motor_dictionary(self) -> list:
        motorDict = utils.get_motor_dict()
        list_of_motions = [motorDict.copy()]
        motorDict["head_left_right"] = 20 * utils.HEAD_RIGHT
        motorDict["head_up_down"] = 20 * utils.HEAD_UP
        motorDict["head_roll"] = 0.0
        motorDict["body_forward"] = 0.0
        motorDict["body_sideways"] = 0.0
        motorDict["body_rotate"] = 0.0
        motorDict["head_left_right"] = 20 * utils.HEAD_LEFT
        motorDict["head_up_down"] = 20 * utils.HEAD_DOWN
        list_of_motions.append(motorDict.copy())

        return list_of_motions

    def move_robot_body(self, forward_backward: int, left_right: int, rotate: int):
        if not self.is_robot_selected():
            return False
        if not self.open_modality("motor"):
            return False

        forward_backward = forward_backward if forward_backward else 0
        left_right = left_right if left_right else 0
        rotate = rotate if rotate else 0
        motorDict = utils.get_motor_dict()
        motorDict["body_forward"] = 1000.0 * forward_backward
        motorDict["body_sideways"] = 1000.0 * left_right
        motorDict["body_rotate"] = 10.0 * rotate

        for i in range(10):
            self.robot.set_modality(
                "motor",
                list(motorDict.values()),
            )

    def say(self, message: str, emotion: str):
        if not self.is_robot_selected():
            return get_missing_robot_response_body()
        if not self.open_modality("speech"):
            return get_unopened_modality_response_body("speech")

        robot_name = self.robot.robot_details.name
        message = message or f"Hi, I am {robot_name}, nice to meet you!"


        try:
            print("message", message)
            speech_outcome = self.robot.set_modality("speech", message)
            if emotion:
                emotion_outcome, emotion_payload = self.robot.set_modality(
                    "emotion", emotion
                )

            if speech_outcome.success:
                return get_success_response_body("Spoke")
            else:
                resp_body = convert_animus_response_to_dict(speech_outcome)
                return resp_body
        except Exception as e:
            message = "Could not speak or express emotion"
            log.error(message, e)
            return get_failure_response_body(message)

    def move_robot_head(self, left_right: int, up_down: int, roll: int):
        if not self.is_robot_selected():
            return get_missing_robot_response_body()
        if not self.open_modality("motor"):
            return get_unopened_modality_response_body("motor")

        left_right = left_right if left_right else 0
        up_down = up_down if up_down else 0
        roll = roll if roll else 0
        motorDict = utils.get_motor_dict()
        motorDict["head_left_right"] = 20 * left_right
        motorDict["head_up_down"] = 20 * up_down
        motorDict["head_roll"] = 5 * roll

        success, result = self.robot.set_modality(
            "motor",
            list(motorDict.values()),
        )

    def start_video_stream(self) -> Generator:
        if not self.is_robot_selected():
            return False
        if not self.open_modality("vision"):
            return False

        self.video_reader = Video_Reader(self.robot)

        return self.video_reader.start_capture

    def stop_video_stream(self) -> bool:
        if self.video_reader:
            self.video_reader.capture = False

        return True

    def demo_motion(self) -> None:
        """ #### Opens a video player showing the robot video feed and moves the head of the robot in 4 random directions and stops. """

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
