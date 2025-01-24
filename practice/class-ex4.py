class unv:
    def __init__(self):
        self.u_name=input('Enter univercity name: ')
        self.u_loc=input('Enter univercity location: ')
    @classmethod
    def u_state(cls):
        cls.unv_state='Odisha'
    '''def u_disp(self):
        print('University name is: {}'.format(self.u_name))
        print('Univercity location is: {}'.format(self.u_loc))'''
class clg:
    def __init__(self):
        self.c_name=input('Enter college name: ')
        self.c_loc=input('Enter college location: ')
    @classmethod
    def c_state(cls):
        cls.clg_state='Bangalore'
    '''def c_disp(self):
        print('College name is: {}'.format(self.c_name))
        print('College location is: {}'.format(self.c_loc))'''
class student(unv,clg):
    unv.u_state()
    clg.c_state()
    def __init__(self,crs='Python'):
        unv.__init__(self)
        clg.__init__(self)
        unv.u_state()
        clg.c_state()
        self.s_no=int(input('Enter student number: '))
        self.s_name=input('Enter student name: ')
        self.course=crs
    def std_dtls(self):
        print('----------------------------------------------------')
        print('\tDetails are below')
        print('-----------------------------------------------------')
        print('Univercity name: {}'.format(self.u_name))
        print('Univercity state location: {}'.format(self.unv_state))
        print('Univercity location: {}'.format(self.u_loc))

        print('College name: {}'.format(self.c_name))
        print('College state location: {}'.format(self.clg_state))
        print('College location: {}'.format(self.c_loc))

        print('Student no: {}'.format(self.s_no))
        print('Student name: {}'.format(self.s_name))
        print('Student course: {}'.format(self.course))

s1=student()
s2=student('Oracle')
s1.std_dtls()
s2.std_dtls()
    
        