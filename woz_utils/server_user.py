class Server_User:

    def __init__(self, username):
        self.username = username
        self.permissions = [
            {
                "USE_TEST_API": False,
                "USE_DEVELOPER_TOOLS": False
            }
        ]
