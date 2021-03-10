from animus_client import *
from loginDetails import LoginDetails

print("setup")
x = setup(None, "", 0)
print(x)

print("login user")
x = login_user(LoginDetails.username, LoginDetails.password, False)
print(x)

print("get robots")
x = get_robots(True, True, False)
print(x)