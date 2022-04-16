
class GenericList:
    def __init__(self, items):
        self._list = items

    def add_2_list(self, item):
        self._list.append(item)

    def __getitem__(self, ind):
        return self._list[ind]

    def sort_list(self):
        self._list.sort()

    def __repr__(self):
        return "<GenericList = {}>".format(str(self._list))


class SortedList(GenericList):
    def __init__(self, items):
        super().__init__(items)
        self.sort_list()

    def add_2_list(self, item):
        super().add_2_list(item)
        self.sort_list()

    def __repr__(self):
        return "<SortedList = {}>".format(str(self._list))
