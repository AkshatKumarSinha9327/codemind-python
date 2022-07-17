n = int(input())
x = list(map(int,input().split()))
a,b = map(int,input().split())
c=0
for i in x:
    if i<a or i>b:
        print(i,end=' ')
        c=1
if not bool(c):
    print(-1)