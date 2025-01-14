while(True):
    while(True):
        r=int(input('Enter student number (1-10) : '))
        if r>=1 and r<=10:
            break
    name=input('Enter student name: ')
    while(True):
        c=int(input('Enter mark for c: '))
        if c>=0 and c<=100:
            break
    while(True):
        o=int(input('Enter mark for oracle: '))
        if o<=100 and o>=0:
            break
    while(True):
        p=int(input('Enter mark for python: '))
        if p>=0 and p<=100:
            break
    print()
    print('=============================================================================')
    print('\t\tMarksheet of {}'.format(name))
    print('=============================================================================')
    print()
    print('\tStudent role no is: {}'.format(r))
    print('\tStudent name is: {}'.format(name))
    print('\tMark got in c: {}'.format(c))
    print('\tMark got in Oracle: {}'.format(o))
    print('\tMark got in python: {}'.format(p))
    print('=============================================================================')
    print('\tTotal marck is: {}'.format(c+o+p))
    print('\tPercentage: {}'.format(round((c+o+p)/300*100)))
    if c<40 or o<40 or p<40:
        print('\tGrade: FAIL')
    else:
        if c+o+p >= 250 and c+o+p <= 300:
            print('\tGrade: DISTICTION')
        elif round((c+o+p)/300*100) >=60:
            print('\tResult: FIRST CLASS')
        elif round((c+o+p)/300*100) >=50 and round((c+o+p)/300*100) < 59:
            print('\tResult: SECOND CLASS')
        elif round((c+o+p)/300*100) >= 40 and round((c+o+p)/300*100) < 49:
            print('\tResult: THIRD CLASS')
        
    print('=============================================================================')
    y=input('Do you want to continue (y/n): ')
    if y.upper() == 'N':
        break