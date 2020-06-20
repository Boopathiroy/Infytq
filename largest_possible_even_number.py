
#IP = Hello#81@21349
#OP = 984312

st = 'Hello#81@21349'
l = sorted(list(set(filter(lambda x: x.isdigit(),st))),reverse=True)
print(l)
even = list(filter(lambda x: int(x)%2==0,l))
print(even)
if len(even)==0:
    print(-1)
else:
    if int(l[-1])%2==0:
        print("".join(l))
    else:
        l.remove(even[-1])
        l.append(even[-1])
print("".join(l))