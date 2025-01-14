while(True):
    age=int(input('Enter your age: '))
    if (age>=18) and (age<=100):
        break
print('{} is correct age'.format(age))