"""
Hello World Module

Usage:
    python mod_04.py <String To Greet>
"""
import sys


def func01(x):
    """Hello Method."""
    print("hello {}".format(x))


def main(arg):
    """
    Main function
    :param arg: String
    :return: Return from function call func01
    """
    func01(arg)


if __name__ == '__main__':
    main(sys.argv[1])
