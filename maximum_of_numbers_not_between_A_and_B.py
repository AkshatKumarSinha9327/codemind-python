n = int(input())
x = list(map(int,input().split()))
a,b = map(int,input().split())
# print(x,a,b)
m = 0
for i in x:
    if (i<a or i>b) and m<i:
        m=i
        # print(i,end=' ')
if m==0:
    print(-1)
else:
    print(m)