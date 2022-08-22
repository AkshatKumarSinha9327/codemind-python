n,m  = map(int,input().split())

a = []

for i in range(n):
    s = 0
    for j in list(map(int,input().split())):
        s+=j
    a.append(s)
print(max(a))