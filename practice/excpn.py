a=input('Enter first value: ')
b=input('Enter second value: ')
try:
    x=int(a)
    y=int(b)
    c=x/y
except ValueError:
    print('Only intiger required')
except ZeroDivisionError:
    print('0 is not divisible')
else:
    print('In else part')
    print(c)
finally:
    print('In finally block')
print('Program executed completly.....')