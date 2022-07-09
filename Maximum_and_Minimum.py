n = int(input())

x = list(map(int,input().split()))
temp = []
for i in x:
    if x.count(i)==i and i not in temp:
        temp.append(i)
if len(temp)==0:
    print(-1)
else:
    print(min(temp),max(temp))