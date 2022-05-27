t,s,b = map(int,input().split())

cap = 2*s*t*b*512
print('{0}KB'.format(int(cap/1024)))