# cat=[str(x) for x in range(10) 'even' if x%2==0 else 'odd']
# print(cat)

even=[x for x in range(51) if x%2==0]
print(even)

cat=['Even' if x%2==0 else 'Odd' for x in range(10)]
print(cat)

