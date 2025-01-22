class student:
    def add_student(self):
        try:
            self.r=int(input('Enter roll number: '))
            self.n=input('Enter student name: ')
            self.c=int(input('Enter class: '))
            self.s=input('Enter section: ')
        except ValueError:
            print('Enter proper value')
    def add_marks(self):
        print('----------------------------------------------------------------------')
        print('\tEnter marks for student: {}'.format(self.n))
        print('----------------------------------------------------------------------')
        self.math=int(input('Enter marks for math: '))
        self.sc=int(input('Enter marks for science: '))
        self.eng=int(input('Enter marks for engilish: '))
    def disp(self):
        print('----------------------------------------------------------------------')
        print('\tShowing result of student: {}'.format(self.n))
        print('\t\tTotal Mark: {}'.format(self.t_mark))
        print('\t\tPercentageis: {}'.format(self.per))
        print('\t\tGrade\t:\t{}'.format(self.grade))
        print('----------------------------------------------------------------------')
        print('\t\tMath\t:\t{}'.format(self.math))
        print('\t\tScince\t:\t{}'.format(self.sc))
        print('\t\tEnglish\t:\t{}'.format(self.eng))

    @classmethod
    def tot_mark(cls,student_instance):
        cls.t_mark=student_instance.math + student_instance.sc + student_instance.eng
        cls.per=(cls.t_mark/300)*100
    @classmethod
    def show_grade(cls):
        if cls.per >= 80:
            cls.grade='Distinction'
        elif cls.per >=60 and cls.per <80:
            cls.grade='First class'
        elif cls.per >= 45 and cls.per < 60:
            cls.grade='Second class'
        elif cls.per >= 30 and cls.per < 45:
            cls.grade='Third class'
        else:
            cls.grade='Fail'

s1=student()
s2=student()

s1.add_student()
s2.add_student()

s1.add_marks()
s2.add_marks()

s1.tot_mark(s1)
s2.tot_mark(s2)

s1.show_grade()
s2.show_grade()

s1.disp()
s2.disp()


        
