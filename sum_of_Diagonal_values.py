n,m = map(int,input().split())

mat = []

for i in range(n):
    mat.append(list(map(int,input().split())))
s=0
for i in range(n):
    for j in range(m):
        if i==j or (j+i)==n-1:
            s+=mat[i][j]
print(s)