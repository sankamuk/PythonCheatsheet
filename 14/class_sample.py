class Man:
  SOCIAL_ID = 0
  @classmethod
  def _get_id(cls):
    cls.SOCIAL_ID += 1
    return cls.SOCIAL_ID
  def __init__(self, name):
    self._name = name
    self._id = Man._get_id()
    self._sex = "male"
    self._working = "yes"
  @property
  def name(self):
    return self._name
  @property
  def id(self):
    return self._id
  @property
  def sex(self):
    return self._sex
  @property
  def working(self):
    return self._working
  @working.setter
  def working(self, w):
    if w != "yes" and w != "no":
        raise Exception("Invalid Input - Could be only yes/no")
    self._working = w
  def greet(self):
    print("Hello World, i am a {0} named {1} with id {2} and working status {3}".format(self.sex,
                                                                                        self.name,
                                                                                        self.id,
                                                                                        self.working))
