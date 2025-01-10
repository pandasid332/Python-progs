'''from collections import Counter

# List of elements
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'pear']

# Count the occurrences of each element using Counter
element_counts = Counter(elements)

# Print the result
print(element_counts)'''

n=int(input('Enter element count: '))
if n<=0:
    print('Don''t give zero or minus value.')
else:
    l=[]
    d={}
    for i in range(1,n+1,1):
        val=input('Enter {} value: '.format(i))
        l.append(val)
    else:
        for i in l:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        else:
            for k,v in d.items():
                print('{} contains {} times'.format(k,v))


