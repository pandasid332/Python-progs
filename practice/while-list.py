lst=[int(x) for x in input('Enter comma separetaed value: ').split(',')]
s=0
i=0
while(i<len(lst)):
    s=s+lst[i]
    i=i+1
else:
    print('Combination of all value is: {}'.format(s))