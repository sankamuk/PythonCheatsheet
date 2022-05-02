
class Host:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Host<{}>".format(self.name)

    def __str__(self):
        return "Host<{}>".format(self.name)

    def host(self, visitor):
        visitor.visit(self)

    def host_visitedby_vistor1(self, visit1):
        print("Host -> {}, Visitor -> {}".format(self, visit1))

    def host_visitedby_vistor2(self, visit2):
        print("Host -> {}, Visitor -> {}".format(self, visit2))


class Visitor:
    pass

class Visitor1(Visitor):
    def __init__(self, name):
        Visitor.__init__(self)
        self.name = name

    def __repr__(self):
        return "Visitor<{}>".format(self.name)

    def __str__(self):
        return "Visitor<{}>".format(self.name)

    def visit(self, host):
        host.host_visitedby_vistor1(self)


class Visitor2(Visitor):
    def __init__(self, name):
        Visitor.__init__(self)
        self.name = name

    def __repr__(self):
        return "Visitor<{}>".format(self.name)

    def __str__(self):
        return "Visitor<{}>".format(self.name)

    def visit(self, host):
        host.host_visitedby_vistor2(self)
