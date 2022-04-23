x = list(map(int,input().split()))

p,r,t = x[0],x[1],x[2]


ci = p*((1 + r/100)**t)
print("{:.2f}".format(ci))