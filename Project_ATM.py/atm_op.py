from data import bal
from excpt import *
from data import *
def bal_inq(u):
    print('Balance in your account is {}'.format(bal.get(u)))
def withdraw_bal(u):
    w=int(input('Enter how much you want to withdraw: '))
    if w>bal.get(u):
        raise LowBalance
    else:
        bal[u]=bal.get(u)-w
        print('New balance is {}'.format(bal.get(u)))
def Deposit_bal(u):
    d=int(input('Enter deposite ammount: '))
    if d>5000:
        raise LargAmmount
    else:
        bal[u]=bal.get(u)+d
        print('Your new balance is: {}'.format(bal.get(u)))
def Change_pin(u):
    while(True):
        p_old=int(input('Enter old pin: '))
        if p_old==user.get(u):
            break
        else:
            print('Wrong pin. Try Again')
    while(True):
        p_new=int(input('Enter new pin: '))
        if p_new >=1000 and p_new != p_old:
            break
        else:
            print('Pin is equal to old pin or length of pin is less then 1000. Try again')
    user[u]=p_new
    print('Your new pin has been ben set.')


