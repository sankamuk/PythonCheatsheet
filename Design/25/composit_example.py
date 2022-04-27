
class Item:
    def __init__(self, *args, **kwargs):
        pass

    def item_function(self):
        pass

class Child(Item):

    def __init__(self, *args, **kwargs):
        Item.__init__(self, *args, **kwargs)
        self.name = args[0]

    def item_function(self):
        print("Name - {}".format(self.name))

class Composite(Item):

    def __init__(self, *args, **kwargs):
        Item.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.childs = []

    def add_child(self, child):
        self.childs.append(child)

    def remove_child(self, child):
        self.childs.remove(child)

    def item_function(self):
        print("Name - {}".format(self.name))
        for c in self.childs:
            c.item_function()


