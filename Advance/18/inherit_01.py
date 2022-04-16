
class Base:
    def __init__(self):
        print("Base Class - Init")

    def func(self):
        print("Base Class - func")


class Child(Base):
    def __init__(self):
        super().__init__()
        print("Child Class - Init")

    def func(self):
        print("Child Class - func")

