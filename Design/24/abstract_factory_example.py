from random import randint


class Man:
    """Man class"""
    def __init__(self, name):
        self._name = name

    def sex(self):
        print("Male")

    def __repr__(self):
        return "Man - {}".format(self._name)


class Woman:
    """Woman class"""
    def __init__(self, name):
        self._name = name

    def sex(self):
        print("Woman")

    def __repr__(self):
        return "Man - {}".format(self._name)


class ManFactory:
    """Concrete Man Factory"""
    def __init__(self):
        self._professions = ["infrastructure", "it", "banking"]

    def get_being(self, name):
        return Man(name)

    def get_profession(self):
        return self._professions[randint(0,2)]


class WomanFactory:
    """Concrete Woman Factory"""
    def __init__(self):
        self._professions = ["house making", "dress", "banking"]

    def get_being(self, name):
        return Woman(name)

    def get_profession(self):
        return self._professions[randint(0, 2)]


class HumanFactory:
    """Abstract Factory"""

    def __init__(self, factory_type=None):
        self._being_factory = factory_type

    def return_being_details(self, name):
        being = self._being_factory.get_being(name)
        being_profession = self._being_factory.get_profession()

        print("Name: {}".format(being))
        print("Works: {}".format(being_profession))

