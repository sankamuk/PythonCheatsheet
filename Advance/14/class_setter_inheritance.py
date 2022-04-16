class Human:
    def __init__(self, name):
        self._name = name
        self._working = "no-work"

    @property
    def name(self):
        return self._name

    @property
    def working(self):
        return self._working

    @working.setter
    def working(self, w):
        if w != "work" and w != "no-work":
            raise Exception("Invalid Input - Could be only work/no-work")
        self._working = w

    def greet(self):
        print("Hello World, i am {0} working status {1}".format(self.name,
                                                                self.working))


class Man(Human):
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return "Man: " + self._name

    @Human.working.setter
    def working(self, w):
        if w != "man-work" and w != "no-work":
            raise Exception("Invalid Input - Could be only man-work/no-work")
        self._working = w
