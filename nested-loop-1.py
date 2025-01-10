n=int(input('Enter how many multiplication table you want: '))
if n<=0:
    print('Invalid input')
else:
    l=[]
    l1=[]
    for i in range(1,n+1,1):
        val=int(input('Enter {} no value: '.format(i)))
        l.append(val)
    for i in l:
        if i<=0:
            l1.append(i)
        else:
            print()
            print('Table for {} below:- '.format(i))
            print('*****************************************************')
            print()
            for j in range(1,11,1):
                print('\t{} * {} = {}'.format(i,j,i*j))
    else:
        print()
        print('For {} numbers table can''t be generated'.format(l1))