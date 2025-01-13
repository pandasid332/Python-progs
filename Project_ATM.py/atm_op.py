from data import bal
from excpt import LowBalance
def bal_inq(u):
    print('Balance in your account is {}'.format(bal.get(u)))
def withdraw_bal(u):
    w=int(input('Enter how much you want to withdraw: '))
    if w>bal.get(u):
        raise LowBalance
    else:
        bal[u]=bal.get(u)-w
        print('New balance is {}'.format(bal.get(u)))
