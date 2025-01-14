d={'aa':1,'bb':2}

t=input('Enter name: ')
if t in d.keys():
    print('{} is availble'.format(t))
    print()
    while(True):
        p=int(input('Enter password: '))
        if p==d.get(t):
            break
        else:
            print('Tr again...')  
    print('{} is successfully logged in.'.format(t))
else:
    print('{} is not available'.format(t))
