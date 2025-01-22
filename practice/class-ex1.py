class student:
    s_class=1
    def add_std(self):
        print('=========================================================')
        self.r=int(input('\tEnter student roll no: '))
        self.n=input('\tEnter student name: ')
        self.m=float(input('\tEnter student mark: '))
        print('=========================================================')
    def disp(self):
        print('Student roll no is: {}'.format(self.r))
        print('Student name is: {}'.format(self.n))
        print('Student mark is: {}'.format(self.m))
        print('Student class is: {}'.format(student.s_class))
        print('Student section is: {}'.format(student.sec))
s1=student()
s2=student()

student.sec='A'

s1.add_std()
s2.add_std()

s1.disp()
s2.disp()