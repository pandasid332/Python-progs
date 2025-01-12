import functools as fn
from func_3 import add_cube

def test(lst):
    print('\tOriginal list is below ')
    print('=================================================')
    for i in lst:
        print('\t{}'.format(i),end=' ')

    pos=list(filter(lambda x : True if x>0 else False,lst))
    neg=list(filter(lambda x : True if x<0 else False,lst))
    print()
    print()
    print('\tPosetive value list is below ')
    print('=================================================')
    for i in pos:
        print('\t{}'.format(i),end=' ')

    print()
    print()
    print('\tNegetive value list is below ')
    print('=================================================')
    for i in neg:
        print('\t{}'.format(i),end=' ')

    cube=list(map(lambda x : x**3,pos))
    sqr=list(map(lambda x : x**2,neg))

    print()
    print()
    print('\tCube of posetive value list is below ')
    print('=================================================')
    for i in cube:
        print('\t{}'.format(i),end=' ')

    print()
    print()
    print('\tSquare of negetive value list is below ')
    print('=================================================')
    for i in sqr:
        print('\t{}'.format(i),end=' ')

    big=fn.reduce(lambda x,y : x if x>y else y,lst)
    small=fn.reduce(lambda x,y : x if x<y else y,lst)

    print()
    print()
    print('\tLargest value in list is below ')
    print('=================================================')
    print('\t{}'.format(big))

    print()
    print()
    print('\tSmallest value in list is below ')
    print('=================================================')
    print('\t{}'.format(small))

    
    add_c=add_cube(cube)
    add_s=add_cube(sqr)

    print()
    print()
    print('\tAddition of cube value in list is below ')
    print('=================================================')
    print('\t{}'.format(add_c))

    print()
    print()
    print('\tAddition of Square value in list is below ')
    print('=================================================')
    print('\t{}'.format(add_s))