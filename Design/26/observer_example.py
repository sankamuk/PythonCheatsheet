
class Subject:
    def __init__(self):
        self._observer = []

    def attach(self, observer):
        self._observer.append(observer)

    def detach(self, observer):
        self._observer.remove(observer)

    def notify(self, modifier=None):
        for obs in self._observer:
            if obs is not modifier:
                obs.update(self)


class Core(Subject):
    def __init__(self, name):
        Subject.__init__(self)
        self._name = name
        self._trait  = 0

    @property
    def trait(self):
        return self._trait

    @trait.setter
    def trait(self, trait):
        self._trait = trait
        self.notify(self)

    def __str__(self):
        return "Core<{}>".format(self._name)

    def __repr__(self):
        return "Core<{}>".format(self._name)


class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, subject=None):
        print("Observer -> {}, Viewed -> {}".format(self.name, subject))



