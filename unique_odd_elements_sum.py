n = int(input())
x = list(map(int,input().split()))
s=0
temp = []
for i in x:
    if i%2==1 and i not in temp:
        s+=i
        temp.append(i)
print(s)