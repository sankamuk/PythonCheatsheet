
class DBHandler:
    def handle_db_action(self):
        print("Performing action")


class ProxyHandler:
    def __init__(self):
        self.db = None
        self.state = 0

    def check_state(self):
        return self.state

    def change_state(self):
        self.state = 0 if self.state else 1

    def wait_now(self):
        print("Handler is busy!")

    def perform_action(self):
        self.db = DBHandler()
        self.db.handle_db_action()

