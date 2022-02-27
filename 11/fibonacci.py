import sys


def fibonacci_number(nth):
    """Find nth Fibonacci number"""
    a, b, c = 0, 1, 1
    if nth == 0:
        return a
    elif nth == 1:
        return b
    else:
        while c == int(nth):
            a, b, c = b, a+b, c+1
        return b


if __name__ == '__main__':
    print("- {}th Fibonacci number is {}".format(sys.argv[1],
                                                 fibonacci_number(sys.argv[1])))
