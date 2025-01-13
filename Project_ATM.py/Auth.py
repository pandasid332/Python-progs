from data import user
from excpt import UserNotPresent
def user_auth():
    u=input('Enter user name: ')
    if u in user.keys():
        print('{} Is available...'.format(u))
        while(True):
            p=int(input('Enter passord for {} : '.format(u)))
            if p == user.get(u):
                break
            else:
                print('Try again....')
        return u
    else:
        raise UserNotPresent
    
# user_auth()