n=int(input('Enter which multiple table you want to genarate: '))
if n==0:
    print('Don''t give zero')
elif (n<0):
    print('Don''t give minus number')
else:
    print('*****************************************************************')
    print('\t\tMultiple table for {} is below'.format(n))
    print('*****************************************************************')
    print()
    i=1
    while(i<=10):
        print('\t\t\t{} * {} = {}'.format(n,i,n*i))
        i=i+1
    else:
        print()
        print('*****************************************************************')