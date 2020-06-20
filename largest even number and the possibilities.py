
#IP = 1,4,2,1
#OP = 421,12

inarr = [x for x in input().split(',')]
inarr.sort(reverse=True)
maxnum = "".join(inarr[:3])

from itertools import permutations

p = set(permutations(inarr,3))
print(maxnum,end=',')
print(len(p))