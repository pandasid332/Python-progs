import functools
class ids:
    def __init__(self,id):
        self.id = id
        self.a=self.display()
    def display(self):
        print()
        print('----------------------INPUT VALUE----------------------')
        for k,v in enumerate(self.id):
            print('\t Key:\t{}\t Value:\t{}'.format(k,v))
        pos=filter(lambda x: True if x>0 else False,self.id)
        l=list(pos)
        l.sort()
        
        print()
        print('----------------------POSETIVE VALUE----------------------')
        for k,v in enumerate(l):
            print('\t Key:\t{}\t Value:\t{}'.format(k,v))
            
        big=functools.reduce(lambda x,y: x if x>y else y,self.id)
        small=functools.reduce(lambda x,y: x if x<y else y,self.id)
        
        return big,small
        
        
def main():        
    n=[int(x) for x in input('Enter comma separated values:').split(',')]
    obj=ids(n)
    print('Biggest value is: {}'.format(obj.a[0]))
    print('Smallest value is: {}'.format(obj.a[1]))

if __name__ == '__main__':
    main()