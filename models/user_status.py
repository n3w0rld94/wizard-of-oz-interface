from animus_wrapper.animus_wrapper import Animus_Client
from woz_utils.proto_converters import proto_obj_list_to_dict
from woz_utils.server_utils import get_failure_response_body

from models.i_animus_response import Animus_Response


class Animus_User:
    def __init__(self, username):
        self.username = username
        self.loggedIn = False
        self.animus_wrapper = Animus_Client()

    def logout(self):
        self.loggedIn = False
        try:
            self.animus_wrapper.dispose_animus()
        except Exception as e:
            print("Error while disposing Animus", e)

    def login(self, username, password) -> Animus_Response:
        outcome = self.animus_wrapper.login(username, password)
        self.loggedIn = outcome["success"]
        return outcome

    def get_available_robots(self):
        robots, errors = self.animus_wrapper.get_robots(True, True, False)
        self.available_robots = robots

        return proto_obj_list_to_dict(robots), errors

    def connect_to_selected_robot(self, robot_id):
        if not robot_id:
            return get_failure_response_body("No robot details were provided")

        for robot in self.available_robots:
            if robot.robot_id == robot_id:
                outcome = self.animus_wrapper.choose_robot(robot)
                if outcome["success"]:
                    return self.animus_wrapper.connect_to_robot()
                else:
                    return outcome

        return get_failure_response_body("Could not find the robot selected")
