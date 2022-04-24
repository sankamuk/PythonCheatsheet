class Director:
    """Director"""
    def __init__(self, builder):
        self._builder = builder

    def construct_working_professional(self):
        self._builder.create_working_professional()
        self._builder.add_sex()
        self._builder.add_specialization()

    def get_working_professional(self):
        return self._builder.being


class AbstractBuilder:
    """Abstract Builder"""
    def __init__(self):
        self.being = None

    def create_working_professional(self):
        self.being = Human("Sankar")


class Builder(AbstractBuilder):
    """Concrete Builder"""
    def add_sex(self):
        self.being.sex = "male"

    def add_specialization(self):
        self.being.specialization = "IT"


class Human:
    """Product"""
    def __init__(self, name):
        self.name = name
        self.sex = None
        self.specialization = None

    def __str__(self):
        return "{} is {} and good in {}".format(self.name, self.sex, self.specialization)
