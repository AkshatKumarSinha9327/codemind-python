n,m = map(int,input().split())

mat = []

for i in range(n):
    mat.append(list(map(int,input().split())))
s=0
for i in range(n):
    for j in range(m):
        if i!=n-1 and j!=m-1 and i!=0 and j!=0:
            s+=mat[i][j]
print(s)