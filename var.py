a=10
b=20

def add():
    global a,b
    ga=globals()['a']
    gb=globals()['b']
    return ga+gb,a+b,a+100,b+100
x=add()
print(len(x))
for i in range(0,len(x)):
    print(x[i])