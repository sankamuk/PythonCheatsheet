
_global_list = []


def add_element(e):
    _global_list.append(e)


def list_elements():
    return iter(_global_list)