
class SampleStructure:
    def __init__(self, n, d):
        self._name = n
        self._data = d
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == len(self._data):
            raise StopIteration()
        self._index += 1
        return self._data[self._index - 1]

    def __str__(self):
        return "List - {}".format(self._name)

    def __repr__(self):
        return "<List:{}>".format(self._name)

