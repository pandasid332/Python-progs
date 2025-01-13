from expn_1 import SidError
from expn_2 import sub
try:
    sub()
except SidError:
    print('Second value can not be zero')