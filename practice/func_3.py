import functools
def add_cube(lst):
    val=functools.reduce(lambda x,y : x+y,lst)
    return val
