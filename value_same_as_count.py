n = int(input())

x = list(map(int,input().split()))
temp = []
for i in x:
    if x.count(i)==i and i not in temp:
        temp.append(i)
print(len(temp))