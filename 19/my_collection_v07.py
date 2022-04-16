
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
