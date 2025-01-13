from menu import menu_op
from oprtion import *
import sys
menu_op()
while(True):
    ch=int(input('\tEnter your choice: '))
    if ch==1:
        r=add()
        print('\tAddition of {} and {} is {}'.format(r[0],r[1],r[2]))
    elif ch==2:
        r=sub()
        print('\tSubstract {} from {} is {}'.format(r[1],r[0],r[2]))
    elif ch==3:
        r=mul()
        print('\tMultipication {} with {} is {}'.format(r[0],r[1],r[2]))
    elif ch==4:
        r=div()
        print('\tDivision {} by {} is {}'.format(r[0],r[1],r[2]))
    elif ch==5:
        r=md()
        print('\tModulo division {} by {} is {}'.format(r[0],r[1],r[2]))
    elif ch==6:
        r=expo()
        print('\t{} power of {} is {}'.format(r[0],r[1],r[2]))
    elif(ch==7):
        sys.exit()


    
    
