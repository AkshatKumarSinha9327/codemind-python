n,m = map(int,input().split())

mat = []

for i in range(n):
    mat.append(list(map(int,input().split())))
    
d = {}
for i in range(m):
    d[i] = 0
for i in range(n):
    for j in range(m):
        d[j] = d[j]+ mat[i][j]

m = 0
for i in d.values():
    if m<i:
        m = i
print(m)