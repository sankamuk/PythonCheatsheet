class Cache:
    _global_dict = dict()

    def __init__(self):
        self._cache = self._global_dict


class Singleton(Cache):
    def __init__(self, kwargs):
        Cache.__init__(self)
        self._global_dict.update(kwargs)

    def __str__(self):
        return str(self._global_dict)

