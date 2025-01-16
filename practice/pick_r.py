import pickle
import os
print(os.getcwd())
file=input('Enter file name: ')

with open(file) as fp:
    try:
        while(True):
            try:
                data=pickle.load(fp)
                for i in data:
                    print('\t{}'.format(i))
            except EOFError:
                print('=========================================================')
                break
    except FileNotFoundError:
        print('File name does not exist')
        