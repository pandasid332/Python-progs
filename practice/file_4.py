s_file=input('Enter source file name: ')
try:
    with open(s_file) as rf:
        d_file=input('Enter destination file name: ')
        with open(d_file,'a') as wf:
            fdata=rf.read()
            wf.write(fdata)
            print('Data writen. pls verify')
except FileNotFoundError:
    print('File does not exist')