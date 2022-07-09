n,m = map(int,input().split())

mat = []

for i in range(n):
    mat.append(list(map(int,input().split())))

mx=0
for i in range(n):
    s = 0
    for j in range(m):
        s+= mat[i][j]
        
    if mx<s:
        mx = s
print(mx)