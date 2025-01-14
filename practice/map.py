
while(True):
    n=int(input('Enter element no: '))
    if n>0:
        break
lst1=[]
lst2=[]

print('Enter value for first list: ')
for i in range(1,n+1):
    val=int(input('Enter {} no. value: '.format(i)))
    lst1.append(val)

print('Enter value for second list: ')
for i in range(1,n+1):
    val=int(input('Enter {} no. value: '.format(i)))
    lst2.append(val)

add_list=list(map(lambda x,y : x+y,lst1,lst2))
print('Addition of two list is: {}'.format(add_list))