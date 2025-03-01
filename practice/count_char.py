n=str(input('Enter a string: '))
d={}
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    print(k,v)
# Output:
# Enter a string: hello
# h 1
# e 1
# l 2
# o 1

print(d['h'])