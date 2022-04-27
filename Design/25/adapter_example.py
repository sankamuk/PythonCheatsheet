
class NumberAdd:

    def add_number(self, a, b):
        return int(a) + int(b)

class StringAdd:

    def add_string(self, a, b):
        return a + b

class Adapter:

    def __init__(self, operator_object, **arg_mapping):
        self._object = operator_object
        self.__dict__.update(arg_mapping)

    def __getattr__(self, item):
        return getattr(self._object, item)