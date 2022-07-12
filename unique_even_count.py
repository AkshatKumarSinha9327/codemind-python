n = int(input())
x = set(map(int,input().split()))
c=0
for i in x:
    if i%2==0:
        c+=1
print(c)