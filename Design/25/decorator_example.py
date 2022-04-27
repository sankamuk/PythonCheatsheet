from functools import wraps


def decorator_example(f):
    @wraps(f)
    def wrap_function():
        return "Hello {}!".format(f())
    return wrap_function


@decorator_example
def greet():
    return "sankar"

