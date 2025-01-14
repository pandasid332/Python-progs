def total_marks(sn,sno,**mark):
    print('----------------------------------------------')
    print('\tName\tNumber')
    print('\t{}\t{}'.format(sn,sno))
    print('-----------------------------------------------')
    print('\tSubject\tMarks')
    print('------------------------------------------------')
    for k,v in mark.items():
        print('\t{}\t{}'.format(k,v))



# Main program

total_marks('aa',10,c=10,o=20,p=30)
total_marks('bb',11,c=10,o=20,p=30,m=40)
total_marks('cc',12,c=10,o=20,p=30,m=40,r=50)
total_marks('dd',13,c=10,o=20,p=30,m=40,r=50,t=60)
