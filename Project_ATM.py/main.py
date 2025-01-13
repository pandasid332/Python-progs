from excpt import *
from Auth import user_auth
from menue import menu_op
from atm_op import *
import sys

try:
    u=user_auth()
except UserNotPresent:
    print('User is not available....')
else:
    print('WELCOME {}'.format(u))
    print('====================================================================================')
    print('\t\t\tW E L C O M E   T O   A T M')
    print('====================================================================================')
    print()
    menu_op()
    c=int(input('Enter your choice: '))
    if c==1:
        bal_inq(u)
    elif c==2:
        try:
            withdraw_bal(u)
        except LowBalance:
            print('Balance is less then input ammount..')
    elif c==5:
        sys.exit()
