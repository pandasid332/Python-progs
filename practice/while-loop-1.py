n=int(input('Enter value: '))
if n==0:
    print('Don''t give Zero ')
else:
    print('**********************************************************')
    print()
    i=1
    while(i<=n):
        print('\t {}'.format(i))
        i=i+1
    else:
        i=-1
        while(i>=n):
            print('\t {}'.format(i))
            i=i-1
        else:
            print()
            print('**********************************************************')