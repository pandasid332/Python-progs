class employee:
    def __init__(self,loc='Bangalore'):
        self.empno=int(input('Enter employee number: '))
        self.ename=input('Enter employee name: ')
        self.dsg=input('Enter employee designation: ')
        self.sal=int(input('Enter employee salary: '))
        self.l=loc
    def emp_disp(self):
        print('\tEmployee no is : {}'.format(self.empno))
        print('\tEmployee name is : {}'.format(self.ename))
        print('\tEmployee designation is : {}'.format(self.dsg))
        print('\tEmployee salary is : {}'.format(self.sal))
        print('\tEmployee location is : {}'.format(self.l))
        print('\tNew salary is : {}'.format(self.sal1))
    @classmethod
    def add_bonus(cls,emp_instance):
        cls.sal1=emp_instance.sal + (emp_instance.sal/100*15)

e1=employee()
e2=employee('Hyderabad')
employee.add_bonus(e1)
print('--------------------------------------------------')
print('\t\tShowing {} details below'.format(e1.ename))
print('--------------------------------------------------')
e1.emp_disp()
employee.add_bonus(e2)
print('--------------------------------------------------')
print('\t\tShowing {} details below'.format(e2.ename))
print('--------------------------------------------------')
e2.emp_disp()