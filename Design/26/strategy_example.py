import types

class ChangeBehaviour:
    def __init__(self, name, behaviour_function=None):
        self.name = name
        if behaviour_function:
            self.execute = types.MethodType(behaviour_function, self)

    def execute(self):
        print("Default behaviour for object - {}".format(self.name))

def behaviour_type_1(self):
    print("Type 1 behaviour for object - {}".format(self.name))

def behaviour_type_2(self):
    print("Type 2 behaviour for object - {}".format(self.name))