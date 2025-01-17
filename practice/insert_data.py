import oracledb
from db_con_obj import db_obj
def new_std(n):
    print(n)
    print(n[0])
    print(n[0][0])
    '''sn=n[0]
    sno=n[1]
    scl=n[2]
    ssec=n[3]
    sm=n[4]'''
    try:
        con=db_obj()
        cur=con.cursor()
        q="insert into student_3 values('%s',%d,%d,'%s',%f)"
        cur.execute(q %(n[0],n[1],n[2],n[3],n[4]))
        con.commit()
    except oracledb.DatabaseError as er:
        print(er)
    else:
        print('1 Row inserted sucessfully...')
    finally:
        cur.close()
        con.close()
        print('Connection closed..')
# Main program
# s_dtls_1=[]
n=int(input('Enter how many student you want to enter: '))
for i in range(1,n+1,1):
    print('\tEnter student details for: {}'.format(i))
    print('============================================================')
    print()
    s_name=input('Enter name: ')
    s_no=int(input('Enter roll no: '))
    s_class=int(input('Enter class: '))
    s_sec=input('Enter section: ')
    s_mark=float(input('Enter mark: '))
    s_dtls=[]
    s_dtls.append(s_name)
    s_dtls.append(s_no)
    s_dtls.append(s_class)
    s_dtls.append(s_sec)
    s_dtls.append(s_mark)
    #s_dtls_1.append(s_dtls)
    new_std(s_dtls)
