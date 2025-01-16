wp=open('std.data','x')

print(type(wp))
print('file is open: {}'.format(wp.mode))
print('file is readable: {}'.format(wp.readable()))
print('file is writeable: {}'.format(wp.writable()))