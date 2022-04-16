from itertools import chain


class MyCollection:
    """A sorted set implementation"""

    def __init__(self, collection=None):
        """Initializer"""
        self._data = sorted(set(collection)) if collection is not None else []

    def __contains__(self, item):
        """Container protocol function"""
        return item in self._data

    def __len__(self):
        """Size protocol function"""
        return len(self._data)

    def __iter__(self):
        """Iterator protocol function"""
        return iter(self._data)

    def __getitem__(self, item):
        """Sequence protocol function"""
        return self._data[item]

    def __eq__(self, other):
        """Equality protocol function"""
        if not isinstance(other, MyCollection):
            return NotImplemented
        return self._data == other._data

    def __ne__(self, other):
        """Inequality protocol function"""
        if not isinstance(other, MyCollection):
            return NotImplemented
        return self._data != other._data

    def index(self, item):
        """Index protocol function"""
        return self._data.index(item)

    def count(self, item):
        """Count protocol function"""
        return self._data.count(item)

    def __reversed__(self):
        """Reverse protocol function"""
        return self._data.__reversed__()

    def __add__(self, other):
        """Addition/Concatination protocol function"""
        return MyCollection(chain(self._data, other))

    def __mul__(self, other):
        """Miltiplication/Repetation protocol function"""
        return self if other > 0 else MyCollection()

    def __rmul__(self, other):
        """Miltiplication/Repetation protocol function"""
        return self if other > 0 else MyCollection()

    def __lt__(self, other):
        """Less than protocol function"""
        return self._data < other._data

    def __and__(self, other):
        """Intersection protocol function"""
        return set(self._data) & set(other._data)

    def __or__(self, other):
        """Union protocol function"""
        return set(self._data) | set(other._data)