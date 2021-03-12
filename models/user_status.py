from animus_wrapper.animus_wrapper import Animus_Client
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
        except:
            print("Issue while disposing of animus")

    def login(self, username, password) -> Animus_Response:
        outcome = self.animus_wrapper.login(username, password)
        if outcome.success:
            self.loggedIn = True

        return outcome

    def get_available_robots(self):
        return self.animus_wrapper.get_robots(True, True, True)
