class ManAction:
    def walk(self):
        print("Walking Man")

class WomanAction:
    def walk(self):
        print("Walking Woman")

class Human:
    def __init__(self, name, human_action):
        self.name = name
        self.action = human_action

    def walk(self):
        self.action.walk()

    def whoami(self):
        print(self.name)

