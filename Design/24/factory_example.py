
class Human:
    """Human base class"""
    def __init__(self, name):
        self._name = name

    def walk(self):
        print("Walking")


class Man(Human):
    """Man class"""
    def __init__(self, name):
        super().__init__(name)

    def sex(self):
        print("Male")


class Woman(Human):
    """Woman class"""
    def __init__(self, name):
        super().__init__(name)

    def sex(self):
        print("Woman")


def get_being(being_type="man"):
    """Factory method"""
    factory = { "man": Man("Dummy"), "woman": Woman("Dummy") }
    return factory[being_type]