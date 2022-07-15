n = int(input())
x = list(map(int,input().split()))
a,b = map(int,input().split())
# print(x,a,b)
temp = []
for i in x:
    if (i<a or i>b):
        temp.append(i)
if bool(len(temp)):
    print(min(temp))
else:
    print(-1)