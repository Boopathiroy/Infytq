# Input format (Name : Code)
#Find the sum of squares of digits from cpde
#if the sum of squares of digits of the code are
# EVEn 0 Then add the last 2 characters in the begining
# ODD - Then add the first character at the end

#IP = abcd:1234,bcdgfhf:127836,sdjks:1245
#OP = cdab cdgfhfb kssdj

input_str = input().split(',')

for i in input_str:
    string,num = i.split(':')
    length = len(string)
    sum =0

    for digit in num:
        sum += (int(digit)**2)

    if (sum%2==0):
        s = string[length-2:length]
        print(s+string[0:length-2],end=' ')
    else:
        s = string[0]
        print(string[1:length]+s,end=' ')