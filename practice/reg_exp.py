import re

str='AB cd 123 !@#$%^&* CD ab 234'
res=re.finditer('[A-Z]',str)
print('\tvalue\tstart\tend')
print('================================================================')
for r in res:
    print('\t{}\t{}\t{}'.format(r.group(),r.start(),r.end()))
res1=re.finditer('[^A-Z]',str)
print()
print('\tvalue\tstart\tend')
print('================================================================')
for r in res1:
    print('\t{}\t{}\t{}'.format(r.group(),r.start(),r.end()))
res2=re.finditer('[a-z]',str)
print()
print('\tvalue\tstart\tend')
print('================================================================')
for r in res2:
    print('\t{}\t{}\t{}'.format(r.group(),r.start(),r.end()))
res3=re.finditer('[^a-z]',str)
print()
print('\tvalue\tstart\tend')
print('================================================================')
for r in res3:
    print('\t{}\t{}\t{}'.format(r.group(),r.start(),r.end()))
res4=re.finditer('[0-9]',str)
print()
print('\tvalue\tstart\tend')
print('================================================================')
for r in res4:
    print('\t{}\t{}\t{}'.format(r.group(),r.start(),r.end()))
res5=re.finditer('[^0-9]',str)
print()
print('\tvalue\tstart\tend')
print('================================================================')
for r in res5:
    print('\t{}\t{}\t{}'.format(r.group(),r.start(),r.end()))
res6=re.finditer('[^A-Za-z0-9 ]',str)
print()
print('\tvalue\tstart\tend')
print('================================================================')
for r in res6:
    print('\t{}\t{}\t{}'.format(r.group(),r.start(),r.end()))