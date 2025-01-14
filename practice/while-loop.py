a=int(input('Enter start value: '))
b=int(input('Enter last value: '))
c=int(input('Enter step: '))
i=0
if c<0:
    while(a>=b):
        print('/n',a)
        a=a+c
elif c>0:
    while(a<=b):
        print('/n',a)
        a=a+c
else:
    print('Somthing wrong in your input')
