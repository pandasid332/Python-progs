from value_add import add_val
def add():
    x,y=add_val('Addition')
    return x,y,x+y
def sub():
    x,y=add_val('Substraction')
    return x,y,x-y
def mul():
    x,y=add_val('Multipication')
    return x,y,x*y
def div():
    x,y=add_val('Division')
    return x,y,x/y
def md():
    x,y=add_val('Modulo division')
    return x,y,x%y
def expo():
    x,y=add_val('Exponintion')
    return x,y,x**y

# p,q,r=add()
# print('Addition of {} and {} is {}'.format(p,q,r))