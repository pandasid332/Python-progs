import functools

class math_pos:
    def __init__(self, o_lst):
        self.pos_lst = o_lst
        self.pos_val = filter(lambda x: x > 0, self.pos_lst)
        self.lst_pos_val = list(self.pos_val)

class math_neg:
    def __init__(self, o1_lst):
        self.neg_val = filter(lambda x: x < 0, o1_lst)
        self.lst_neg_val = list(self.neg_val)

class cube(math_pos):
    def __init__(self, l):
        super().__init__(l)
        self.cube = map(lambda x: x**3, self.lst_pos_val)
        self.lst_cube = list(self.cube)

class add(cube):
    def __init__(self, add_lst):
        super().__init__(add_lst)
        self.n_add = functools.reduce(lambda x, y: x + y, add_lst)
        self.cube_add = functools.reduce(lambda x, y: x + y, self.lst_cube)

class disp(add, math_neg):
    def __init__(self, add_lst):
        add.__init__(self, add_lst)
        math_neg.__init__(self, add_lst)

    def disp_dtls(self, add_lst):
        self.__init__(add_lst)
        print('\tGiven values are: {}'.format(add_lst))
        print('\tPositive values: {}'.format(self.lst_pos_val))
        print('\tNegative values: {}'.format(self.lst_neg_val))
        print('\tCube of positive values: {}'.format(self.lst_cube))
        print('\tSum of all values: {}'.format(self.n_add))
        print('\tSum of cubes: {}'.format(self.cube_add))

lst = [int(x) for x in input('Enter comma-separated values: ').split(',')]
m1 = disp(lst)
m1.disp_dtls(lst)
i