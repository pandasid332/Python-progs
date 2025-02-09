class circle:
    def __init__(self,r):
        self.r=r
        print('\tThis is constuctor in circle class')
        print('\tRedious is: {}'.format(self.r))
    def draw(self):
        print('\tThis is draw method from circle class')


class triangle:
    def __init__(self):
        print('\tThis is constuctor from triangle class')
    def draw(self):
        print('\tThis is draw method from triange class')


class rect:
    def __init__(self):
        print('\tThis is constuctor from rect class')
    def draw(self):
        print('\tThis is draw method from rect class')


class squre(circle,triangle,rect):
    def __init__(self):
        circle.__init__(self,5.6)
        triangle.__init__(self)
        rect.__init__(self)
        print('\tThis is constuctor from squre class')
    def draw(self):
        circle.draw(self)
        triangle.draw(self)
        rect.draw(self)
        print('\tThis is draw method from squre class')


s1=squre()
s1.draw()