"""
    A sample code to simulate profiler validation
"""
import time


def fetch_user_password(user_name):
    """Fetch password for a user"""
    time.sleep(1)
    return "DUMMY"

@profile
def login_user(user_name, user_secret):
    """Validate a users user & password"""
    print("Try login for user {}.".format(user_name))
    time.sleep(2)
    if fetch_user_password(user_name) == user_secret:
        print("Success")
        return 0
    else:
        print("Failed")
        return 1


def main_app():
    """Main application"""
    for i in range(2):
        login_user(i, "DUMMY")


# Main
if __name__ == '__main__':
    print("Running application.")
    main_app()

