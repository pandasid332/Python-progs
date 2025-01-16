with open('file.data','a') as p:
    print('file open in {} mode'.format(p.mode))
    print('file is readable: {}'.format(p.readable()))
    print('file is writeable: {}'.format(p.writable()))
    print('file is closed: {}'.format(p.closed))
print('out of with block')
print('file is closed {}'.format(p.closed))