n = int(input())
x = list(map(int,input().split()))

a,b = map(int,input().split())
mc = 0
for i in x:
    if i<a or i >b:
        if mc<i:
            mc=i
if mc==0:
    print(-1)
else:
    print(mc)