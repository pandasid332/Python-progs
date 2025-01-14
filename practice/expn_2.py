from expn_1 import SidError
def sub():
    a=int(input('Enter first value: '))
    b=int(input('Enter second value: '))
    if b==0:
        raise SidError
    else:
        c=a/b
        print(c)