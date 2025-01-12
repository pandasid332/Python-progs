add=lambda x=int(input('Enter first value: ')),y=int(input('Enter second value: ')) : x+y
big=lambda x=float(input('Enter first name: ')),y=float(input('Enter second value' )) : x if x>y else y  # Turnery operator

lst=[10,-20]
obj=filter(lambda x : True if x>0 else False,lst)
print(list(obj))

x=add()
print(x)
x=big()
print(x)