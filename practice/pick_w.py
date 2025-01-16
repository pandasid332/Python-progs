import pickle
n=int(input('Enter student no.  :'))
with open(input('Enter file name: '),'ab') as fp:
    for i in range(1,n+1,1):
        print('Enter {} no student details: '.format(i))
        print('==================================================================')
        print()
        sname=input('Enter student name: ')
        sno=input('Enter student no.: ')
        smark=float(input('Enter student mark: '))
        lst=[]
        lst.append(sname)
        lst.append(sno)
        lst.append(smark)
        pickle.dump(lst,fp)
        print('{} Student entered successfully. '.format(sname))
        print('====================================================================')
