def asc_ord(lst):
    lst.sort()
    return lst

def dsc_ord(lst):
    lst.sort(reverse=True)
    return lst

# Manin program

while(True):
    n=int(input('Enter how many numbers you want: '))
    if n>0:
        break
l=[]
for i in range(1,n+1,1):
    val=int(input('Enter {} no value: '.format(i)))
    l.append(val)
x=asc_ord(l)
print()
print('Maximum value is: {}'.format(x[len(x)-1]))
print('Minimum value is: {}'.format(x[0]))
print()
print('=========Ascending Order==================')
for i in x:
    print('\t{}'.format(i))
y=dsc_ord(l)
print()
print('=========Descending Order==================')
for i in y:
    print('\t{}'.format(i))
