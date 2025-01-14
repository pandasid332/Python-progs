# obj=filter(lambda x : True if x>0 else False,[float(x) for x in input('Enter comma separated value: ').split(',')])
# print('Psetive values are: {}'.format(list(obj)))

# print('Negetive values are: {}'.format(list(filter(lambda x : True if x<0 else False,[float(i) for i in input('Enter comma separated value: ').split(',')]))))

print('Enter comma separated value:- ')
lst=[float(x) for x in input().split(',')]
pos=list(filter(lambda x : True if x>0 else False,lst))
print('Posetive values are: {}'.format(list(pos)))
neg=list(filter(lambda x : True if x<0 else False,lst))
print('Negetive values are: {}'.format(list(neg)))


sq=map(lambda x : x**3,pos)
print('Cube of posetive numbers are: {}'.format(list(sq)))
cu=map(lambda x : x**2,neg)
print('Squre of all negetive numbers are: {}'.format(list(cu)))

'''print('Enter comma separated values:- ')
lst = [float(x) for x in input().split(',')]
pos = filter(lambda x: x > 0, lst)
print('Positive values are: {}'.format(list(pos)))'''

'''
print('Enter comma separated values:- ')
lst = [float(x) for x in input().split(',')]

pos = list(filter(lambda x: True if x > 0 else False, lst))
print('Positive values are: {}'.format(pos))

neg = list(filter(lambda x: True if x < 0 else False, lst))
print('Negative values are: {}'.format(neg))

sq = list(map(lambda x: x ** 3, pos))
print('Cube of positive numbers are: {}'.format(sq))

cu = list(map(lambda x: x ** 2, neg))
print('Square of all negative numbers are: {}'.format(cu))'''


