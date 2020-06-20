
#IP = 'google'
#OP = elog

#1st Method
def removing_reversing(str1):
    rem = list(dict.fromkeys(str1,1))
    reversed_list = rem[::-1]
    return ("".join(reversed_list))
string = 'google'
print(removing_reversing(string))

#2nd Method
def rem_rev(str2):
    s = ''
    for i in str2:
        if i not in s:
            s =s+i
    return s[::-1]
string = 'google'
print(rem_rev(string))

str3 = 'python'
print(str3[::-1])

