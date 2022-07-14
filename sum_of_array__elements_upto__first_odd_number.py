n = int(input())
x = list(map(int,input().split()))

s = 0
for i in x:
    if i%2==1:
        break
    s+=i
print(s)