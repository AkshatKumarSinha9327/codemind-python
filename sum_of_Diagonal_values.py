m,n = map(int,input().split())
mat = []
for i in range(m):
    t = list(map(int,input().split()))
    mat.append(t)
# print(mat)
sum=0
temp = []
for i in range(m):
    for j in range(n):
        if (i==j or i+j==m-1 )and [i,j] not in temp:
            temp.append([i,j])
            # print(temp)
            sum+= mat[i][j]
print(sum)
# for i in temp:
#     print(i)