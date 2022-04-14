x = list(map(float,input().split()))

p = x[0]
r = x[1]
t = x[2]
ci = p * ( 1 + ( r / 100 ) ) ** t 

print('{:.2f}'.format(ci))