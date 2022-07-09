n,m = map(int,input().split())

mat = []
d = {}

for i in range(n):
    mat.append(list(map(int,input().split())))
    
for i in range(m):
    d[i] = 0

for i in range(n):
    for j in range(m):
        d[j] = d[j] + mat[i][j]
for i in d.values():
    print(i,end=' ')