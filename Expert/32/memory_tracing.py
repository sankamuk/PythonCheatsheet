"""
    Tracing Memory
"""
import tracemalloc


class ListStorage:
    def __init__(self, _list):
        self.int_list = _list

    def print_data(self):
        for i in self.int_list:
            print(i)


if __name__ == '__main__':
    tracemalloc.start()
    print("First list creation.")
    l1 = ListStorage([1,2])
    print("Second list creation.")
    l2 = ListStorage(range(10000))
    l1.print_data()
    snap = tracemalloc.take_snapshot()

    for s in snap.statistics('lineno'):
        print(s)
