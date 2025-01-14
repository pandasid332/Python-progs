n=int(input('Enter no of elements: '))
if n<=0:
    print('Don''t give zero or minus value')
else:
    l=[]
    for i in range(1,n+1,1):
        val=float(input('Enter {} no value: '.format(i)))
        l.append(val)
    else:
        print(l)
        l.sort()
        print(l)
        l.sort(reverse=True)
        print(l)