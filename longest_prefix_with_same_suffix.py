
#longest_prefix with the same suffix

#IP = abcdabc
#OP = 3

inp_str = input("enter a string:")
n = len(inp_str)
half = n//2

for i in range(half,-1,-1):
    str_prefix = inp_str[0:i]
    str_suffix = inp_str[n-i:n]
    if str_prefix == "" or str_suffix == "":
        print(-1)
        break
    if str_prefix == str_suffix:
        print(len(str_prefix))
        break