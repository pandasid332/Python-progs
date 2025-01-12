import functools
while(True):
    n=int(input('Enter number: '))
    if n>0:
        break
lst=[]
for i in range(1,n+1,1):
    lst.append(i)
add=functools.reduce(lambda x,y : x+y,lst)
print(add)