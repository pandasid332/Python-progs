n=int(input('Enter no of element: '))
if n<=0:
    print('Don''t give zero or minus value')
else:
    l=[]
    '''
    i=1
    while(i<=n):
        a=int(input('Enter value no {}: '.format(i)))
        l.append(a)
        i=i+1 '''
    for i in range(1,n+1,1):
        val=int(input('Enter value no {}: '.format(i)))
        l.append(val)
    else:
        print('Value entered:- ')
        s=0
        for i in l:
            print('\t{}'.format(i),end=' ')
            print()
            s=s+i
        else:
            print('Addition of all {} values is: {}'.format(n,s))
            print('Avarage of all {} values is: {}'.format(n,s/n))
            