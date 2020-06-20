
# IP = #ab$is
#OP = #si$ba

s = '#ab$is'
s1 =""
for i in range(len(s)-1,-1,-1):
    if s[i].isalpha():
        s1 = s1+s[i]
s1=list(s1)
print(s1)
for i in range(len(s)):
    if s[i].isalpha()==False:
        s1.insert(i,s[i])
print("".join(s1))