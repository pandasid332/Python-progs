import oracledb
from datetime import datetime
class new_std:
    def __init__(self,user,pwd,dns):
        try:
            con=oracledb.connect(user=user,password=pwd,dsn=dns)
        except oracledb.DatabaseError as e:
            print('Connection error: {}'.format(e))
        else:
            print('Connection sucessfull..')
            self.new_std()
            cur=con.cursor()
            self.n_std=cur.callfunc('pk_new_std.f_new_std',oracledb.NUMBER,
                         [self.s_fname,self.s_lname,self.dob,self.s_addr])
            print('New student created in database')
            con.commit()
            self.disp()
        finally:
            if cur:
                cur.close()
            if con:
                con.close()
            
    def new_std(self):
        self.s_fname=input('Enter first name: ')
        self.s_lname=input('Enter last name: ')
        # self.s_dob=input('Enter date of birth (DD/MM/YYYY): ')
        try:
            self.dob=datetime.strptime(input('Enter date of birth (DD/MM/YYYY): '),'%d/%m/%Y')
        except ValueError:
            print('Enter correct format date....')
        self.s_addr=input('Enter address: ')
        
    def disp(self):
        print('New student id is: {}'.format(self.n_std))
        print('First name: {}'.format(self.s_fname))
        print('Last name: {}'.format(self.s_lname))
        print('date of birth: {}'.format(self.dob))

new_std('school','school','localhost:1521/orclpdb')
