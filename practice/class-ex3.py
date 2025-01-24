class emp:
    def __init__(self):
        self.r=int(input('Enter emp no: '))
        self.n=input('Enter emp name: ')
    def e_disp(self):
        print('Emp no is: {}'.format(self.r))
        print('Emp name is: {}'.format(self.n))

n=int(input('Enter no of emp: '))
for i in range(1,n+1.1):
    e+str(i)=emp()