
class ASimpleClass:

    def __init__(self):
        self._some_container = []

    def __call__(self, *args, **kwargs):
        print(self._some_container)

    def add_to_container(self, e):
        self._some_container.append(e)