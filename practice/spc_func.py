import functools
class math_pos:
    def __init__(self,o_lst):
        self.pos_lst=o_lst
        self.pos_val=filter(lambda x : True if x > 0 else False,self.pos_lst)
        self.lst_pos_val=list(self.pos_val)
    '''def disp(self):
        print(self.lst_pos_val)'''
class math_neg:
    def __init__(self,o1_lst):
        self.neg_val=filter(lambda x : True if x<0 else False,o1_lst)
        self.lst_neg_val=list(self.neg_val)
        # iprint(self.lst_neg_val)

class cube(math_pos):
    def __init__(self,l):
        super().__init__(l)
        self.cube=map(lambda x : x**3,self.lst_pos_val)
        self.lst_cube=list(self.cube)
        # print(self.lst_cube)
class add(cube):
    def __init__(self, add_lst):
        super().__init__(add_lst)
        # math_pos.__init__(self,add_lst)
        self.n_add=functools.reduce(lambda x,y : x+y,add_lst)
        self.cube_add=functools.reduce(lambda x,y : x+y,self.lst_cube)

class disp(add,math_neg):
    def disp_dtls(self,add_lst):
        add.__init__(self,add_lst)
        print('\tGiven values are : {}'.format(add_lst))

    

lst=[int(x) for x in input('Enter comma separated values: ').split(',')]
# lst1=[int(x) for x in input('Enter comma separated values: ').split(',')]
m1=disp()
# m2=disp()
m1.disp_dtls(lst)
# m2.disp_dtls(lst1)

# m1.disp()
