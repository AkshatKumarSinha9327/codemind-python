n = int(input())

x = list(map(int,input().split()))
s = 0
temp = []
for i in x:
    if x.count(i)==i and i not in temp:
        s+=i
        temp.append(i)

if len(temp)==0:
    print(-1)
else:
    print('{:.2f}'.format(s/len(temp)))