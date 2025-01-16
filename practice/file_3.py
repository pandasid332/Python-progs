'''lst=[]
n=int(input('Enter how many student needs to enter: '))
for i in range(1,n+1,1):
    s_name=input('Enter {} no. student name: '.format(i))
    s_class=input('Enter {} no. student class: '.format(i))
    s_sec=input('Enter {} no. student section: '.format(i))
    lst.append(s_name)
    lst.append(s_class)
    lst.append(s_sec)
    with open('std.txt','a') as ap:
        ap.write(str(lst)+'\n')
    lst=[]'''
with open('std.csv','r') as fp:
    fdata=fp.read()
    print(fdata)
    '''fdata1=fp.readline()
    print(fdata1)
    fdata2=fp.readlines()
    print(fdata2)'''