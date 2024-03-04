n =5
s =0
for i in range(n+1):
    x = lambda i: i*i
    s += x(i)
print("S = {}".format(s))