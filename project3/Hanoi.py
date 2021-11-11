import time
from Stack import Stack

def Hanoi_rec(n, s, a, d):
    print(n, s, a, d)
  # TODO replace pass with your base and recursive cases.
  #base case: n = 0
    if n == 0:
        d.push(s.pop())
    else:
        Hanoi_rec(n = n - 1, s = s, d = a, a = d) #call tower of Hanoi Recursion Function with
        #the auxiliary peg as the destination and the destination peg as the auxiliary, to move
        #every disk which is not the bottom disk onto the Auxiliary peg.
        d.push(s.pop()) #Move bottom disk to the destination
        Hanoi_rec(n = n - 1, s = a, d = d, a = s) #Call the Tower of Hanoi Recursion Function again, sourced from the auxiliary,
        #Where all disks but the bottom disk are stored. Using the recursion, move all of these disks
        #To place them on top of the bottom disk, which is already at the destination.

    print(n, s, a, d)
    print()

def Hanoi(n):
    source = Stack()
    dest = Stack()
    aux = Stack()
    i = n-1
    while i >= 0:
        source.push(i)
        i = i - 1
    Hanoi_rec(n-1, source, aux, dest)

if __name__ == '__main__':
    start = time.time()
    n = 5
    Hanoi(n)
    end = time.time()
    print('computed Hanoi(' + str(n) + ') in ' + str(end - start) + ' seconds.')
