import sys


def func01(x):
    print("hello {}".format(x))


def main(arg):
    func01(arg)


if __name__ == '__main__':
    main(sys.argv[1])
