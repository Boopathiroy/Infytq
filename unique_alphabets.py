#similar,ground,heaven,hell,earth,liar,helf
arr = [x for x in input().split(',')]
l =[]
c=0

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        l.append((arr[i],arr[j]))

for i,j in l:
    if len(set(i+j)) in (len(set(i)),len(set(j))):
        c+=1
        print((i,j))
if c:
    print(c)
else:
    print(-1)

