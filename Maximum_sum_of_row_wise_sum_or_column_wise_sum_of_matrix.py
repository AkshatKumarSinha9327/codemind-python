n,m = map(int,input().split())

a= []

for i in range(n):
    s=0 
    r = list(map(int,input().split()))
    for k in r:
        s+=k
    a.append(s)
print(max(a))