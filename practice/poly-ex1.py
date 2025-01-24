class circle:
    def __init__(self):
        print('Constroctoter from circle class')
    def draw(self):
        print('Drawing circle - it is in circle class')
class rect(circle):
    def __init__(self):
        super().__init__()
        print('Constroctoter from rect class')
    def draw(self):
        super().draw()
        print('Drawing rectangle - it is in rect class')
class square(rect): 
    def __init__(self):
        super().__init__()
        print('Constroctoter from square class')
    def draw(self):
        super().draw()
        print('Drawing square - it is in square class')

s1=square()