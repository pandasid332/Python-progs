n=int(input('Enter how many multiplication table you want: '))
if n<=0:
    print('Don''t give zero or negetive valu')
else:
    l=[]
    for i in range(1,n+1,1):
        val=int(input('Enter {} no value: '.format(i)))
        l.append(val)
    else:
        for i in l:
            print('Table for {} below'.format(i))
            print('*************************************************')
            print()
            for j in range(1,11,1):
                print('\t{} * {} = {}'.format(i,j,i*j))
            else:
                print()