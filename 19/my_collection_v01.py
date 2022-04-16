
class MyCollection:
    """A sorted set implementation"""

    def __init__(self, collection=None):
        """Initializer"""
        self._data = sorted(set(collection)) if collection is not None else []