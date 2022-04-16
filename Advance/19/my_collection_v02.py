
class MyCollection:
    """A sorted set implementation"""

    def __init__(self, collection=None):
        """Initializer"""
        self._data = sorted(set(collection)) if collection is not None else []

    def __contains__(self, item):
        """Container protocol function"""
        return item in self._data
