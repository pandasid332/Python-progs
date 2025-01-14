from excpt import *
from Auth import user_auth
from menue import menu_op
from atm_op import *
import sys

print('====================================================================================')
print('\t\t\tW E L C O M E   T O   A T M')
print('====================================================================================')

try:
    u=user_auth()
except UserNotPresent:
    print('User is not available....')
else:
    print('WELCOME {}'.format(u))
    print()
    while(True):
        menu_op()
        c=int(input('Enter your choice: '))
        if c==1:
            bal_inq(u)
        elif c==2:
            try:
                withdraw_bal(u)
            except LowBalance:
                print('Balance is less then input ammount..')
        elif c==3:
            try:
                Deposit_bal(u)
            except LargAmmount:
                print('More then 5000 can not be deposited.')
        elif c==4:
            Change_pin(u)
        elif c==5:
            sys.exit()
        i=input('Do you want to continue (y/n): ')
        if i.upper()=='Y':
            continue
        elif i.upper()=='N':
            break
        else:
            print('Wrong input')
            sys.exit()
    

