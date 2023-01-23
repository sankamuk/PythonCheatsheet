import sys, os
sys.path.append(os.path.join(sys.path[0], '..'))
from utils.utility import hello


def greet(name):
    """Greet someone"""
    return "{} Good morning.".format(hello(name))


if __name__ == '__main__':
    print(greet("sankar"))

