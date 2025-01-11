add=lambda x=int(input('Enter first value: ')),y=int(input('Enter second value: ')) : x+y
big=lambda x=float(input('Enter first name: ')),y=float(input('Enter second value')) : x if x>y else y

x=add()
print(x)
x=big()
print(x)