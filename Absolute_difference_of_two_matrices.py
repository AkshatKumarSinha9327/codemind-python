n = int(input())
m = []
m1 = []
for i in range(n):
    m.append(list(map(int,input().split())))
    
for i in range(n):
    m1.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if j!=n-1:
            print(abs(m[i][j]-m1[i][j]),end=' ')
        else:
            print(abs(m[i][j]-m1[i][j]))