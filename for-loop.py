lst=[10,20,30]
tpl=(11,12,13)
dct={1:'India',2:'Srilanka',3:'Bhutan'}

for i in lst:
    print('{}'.format(i),end=' ')
print()
for i in lst:
    print('Value in list: {}'.format(i))

for i in tpl:
    print('Value in tupple: {}'.format(i))

for i in dct.keys():
    print('Keys are: {}'.format(i))

for i in dct.values():
    print('Values are: {}'.format(i))

for k,v in dct.items():
    print('Key is: {} and value is: {}'.format(k,v))