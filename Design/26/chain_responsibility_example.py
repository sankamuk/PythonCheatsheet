
class Parent:
    def __init__(self, child):
        self._child = child

    def handle_request(self, request):
        if not self._handle(request):
            return self._child.handle_request(request)

    def _handle(self, request):
        raise NotImplementedError("This is abstract")


class Implementation1(Parent):
    def _handle(self, request):
        if request < 10:
            print("Request less than 10, thus Implementation1 handles request")
            return True

class Implementation2(Parent):
    def _handle(self, request):
        if request < 50:
            print("Request less than 50 but more than 10, thus Implementation2 handles request")
            return True