
def gen(stp, itr):
    c = 0
    for i in itr:
        if c == stp:
            return
        c += 1
        yield i


def run_l():
    l = [1, 2, 3, 4, 5]
    for itm in gen(3, l):
        print(itm)


if __name__ == '__main__':
    run_l()