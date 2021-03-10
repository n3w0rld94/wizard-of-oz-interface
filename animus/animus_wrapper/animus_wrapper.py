# # -*- coding: utf-8 -*-
# # Copyright (c) 2020, Cyberselves Universal Ltd.
# # All Rights Reserved


class Animus_Client:
    a = None

# from models.i_animus_response import Animus_Response
# from models.i_login_details import Animus_Login_Details
# import animus_client as animus
# import animus_utils.animus_utils as utils
# import logging
# import numpy as np
# import random
# import cv2
# import time
# from models.modalities import Robot_Modality

# stopFlag = False

# log = utils.create_logger("MyAnimusApp", logging.INFO)
# log.info(animus.version())


# class Animus_Client:
#     """ A wrapper to the Animus client functionalities """

#     def __init__(self, robot: animus.Robot) -> animus.Robot:
#         self.robot = robot
#         self.setup()

#     def setup(self):
#         audio_params = utils.AudioParams(
#             Backends=["notinternal"],
#             SampleRate=16000,
#             Channels=1,
#             SizeInFrames=True,
#             TransmitRate=30,
#         )
#         setup_result = animus.setup(
#             audio_params=audio_params, logdir="PythonAnimusBasics", loglatency=True
#         )
#         if not setup_result.success:
#             log.error(
#                 "Animus Client - Could not setup Animus SDK, reason: "
#                 + setup_result.description
#             )
#             return False
#         self.setup_motor_dictionary()

#     def login(self, username: str, password: str) -> Animus_Response:
#         if not username or not password:
#             username = Animus_Login_Details.username
#             password = Animus_Login_Details.password

#         login_result = animus.login_user(username, password, system_login=False)
#         if login_result.success:
#             log.info("Animus Client - Login Success")
#             return login_result
#         else:
#             log.info(
#                 "Animus Client - Login Failed. Reason: " + login_result.description
#             )
#             return login_result

#     def get_robots(self, get_local: bool, get_remote: bool, get_system: bool) -> list:
#         get_robots_result = animus.get_robots(get_local, get_remote, get_system)

#         if not get_robots_result.localSearchError.success:
#             log.error(
#                 "Local network search failed: "
#                 + get_robots_result.localSearchError.description
#             )

#         if not get_robots_result.remoteSearchError.success:
#             log.error(
#                 "Remote search failed: "
#                 + get_robots_result.remoteSearchError.description
#             )

#         if len(get_robots_result.robots) == 0:
#             log.info("Animus Client - No Robots found")
#             return []
#         else:
#             return get_robots_result.robots

#     # Parameter passed should looks like so: available_robots.robots[chosen_index]
#     ## TODO: Create Class for robot_details
#     def choose_robot(self, robot_details) -> bool:
#         if not robot_details:
#             log.warn("No robot selected. please chose a robot and try again.")
#             return False

#         self.robot = animus.Robot(robot_details)

#         return True

#     def connect_to_robot(self):
#         if not self.is_robot_selected():
#             return False

#         robot_name = self.robot.robot_details.name
#         connection_result = self.robot.connect()

#         if not connection_result.success:
#             log.warn(
#                 f"Could not connect with robot {robot_name}. Reason: "
#                 + connection_result.description
#             )
#             return False

#         log.info(f"Successfully connected to robot {robot_name}")
#         return True

#     def is_robot_selected(self):
#         if not self.robot:
#             log.warn(
#                 "No robot selected. You must select a robot first in order to perform this action."
#             )
#             return False

#     def open_modality(self, modality_name):
#         """#### Opens a modality channel
#         #### Args:
#                     `modality_name (str)`: The modality channel
#         """

#         if not self.is_robot_selected():
#             return False

#         robot_name = self.robot.robot_details.name
#         open_modality_result = self.robot.open_modality(modality_name)

#         if not self.robot.open_modality(modality_name):
#             log.error(
#                 f"Could not open {modality_name} modality on {robot_name}. Reason: "
#                 + open_modality_result.description
#             )
#             return False

#         log.info(f"Successfully opened {modality_name} modality on {robot_name}")

#         return True

#     def list_available_emotions(self):
#         log.info(utils.emotions_list)

#         return True

#     def list_available_motions(self) -> None:
#         motion_dictionary = utils.get_motor_dict()
#         motion_list = list(motion_dictionary.keys)

#         log.info("------ List of built-in motions ---- ")
#         log.info(motion_list)

#     def dispose_animus(self):
#         if self.robot:
#             self.robot.disconnect()
#         animus.close_client_interface()

#     def demo_speech(self, message: str) -> bool:
#         if not self.is_robot_selected():
#             return False

#         try:
#             robot_name = self.robot.robot_details.name
#             message = message or input(f"Hi, I am {robot_name}, nice to meet you!")
#             self.robot.set_modality(Robot_Modality.SPEECH, message)
#             self.robot.set_modality(
#                 Robot_Modality.EMOTION, random.choice(utils.emotions_list)
#             )
#         except KeyboardInterrupt:
#             log.info("Animus Client - Demo Speech interrupted")
#             return False
#         except SystemExit:
#             log.info("Animus Client - Demo Speech interrupted")
#             return False

#         return True

#     def setup_motor_dictionary(self) -> list:
#         motorDict = utils.get_motor_dict()
#         list_of_motions = [motorDict.copy()]
#         motorDict["head_left_right"] = 2 * utils.HEAD_RIGHT
#         motorDict["head_up_down"] = 2 * utils.HEAD_UP
#         motorDict["head_roll"] = 0.0
#         motorDict["body_forward"] = 0.0
#         motorDict["body_sideways"] = 0.0
#         motorDict["body_rotate"] = 0.0
#         motorDict["head_left_right"] = 2 * utils.HEAD_LEFT
#         motorDict["head_up_down"] = 2 * utils.HEAD_DOWN
#         list_of_motions.append(motorDict.copy())

#         return list_of_motions

#     def demo_motion(self) -> None:
#         """ #### Opens a video player showing the robot video feed and moves the head of the robot in 4 random directions and stops. """

#         num_of_received_images = 0
#         next_motion_index = 0

#         try:
#             cv2.namedWindow("Robot View")
#             while next_motion_index < 4:
#                 image_list, response = self.robot.get_modality("vision", True)
#                 if response.success:
#                     cv2.imshow("RobotView", image_list[0].image)
#                     delay = cv2.waitKey(1)

#                     if delay == 27:
#                         break
#                     num_of_received_images += 1

#                     if num_of_received_images > 100:
#                         num_of_received_images = 0

#                         if next_motion_index >= len(self.list_of_motions):
#                             break

#                         self.robot.set_modality(
#                             Robot_Modality.MOTOR,
#                             list(self.list_of_motions[next_motion_index].values()),
#                         )

#                         next_motion_index += 1
#         except KeyboardInterrupt:
#             cv2.destroyAllWindows()
#         except SystemExit:
#             cv2.destroyAllWindows()

#         cv2.destroyAllWindows()
