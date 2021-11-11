from Stack import Stack

bob = [k for k in range(0,10)]
mary = Stack()
for k in bob:
    mary.push(k)
    print(mary)
for k in bob:
    print(mary.pop())
    print(mary)
    
