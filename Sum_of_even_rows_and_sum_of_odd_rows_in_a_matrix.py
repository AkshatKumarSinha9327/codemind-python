n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

osum = esum = 0

for i in range(n):
    for j in range(m):
        if i%2==0:
            esum+=mat[i][j]
        else:
            osum+= mat[i][j]
print(esum,osum)