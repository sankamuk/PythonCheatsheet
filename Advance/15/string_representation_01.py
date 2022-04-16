
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return "Human- Name: {0}, Age: {1}, Sex: {2}".format(self.name, self.age, self.sex)

    def __repr__(self):
        return "I am a {2} of age {1} called as {0}".format(self.name, self.age, self.sex)
