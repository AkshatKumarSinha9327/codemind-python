n,m = map(int,input().split())

mat = []

for i in range(n):
    mat.append(list(map(int,input().split())))
s=0
for i in range(n):
    for j in range(m-1):
        if mat[i][j]>=mat[i][j+1]:
            break
    else:
        s+=1
for i in range(n):
    for j in range(m-1):
        if mat[i][j]<=mat[i][j+1]:
            break
    else:
        s+=1
print(s)