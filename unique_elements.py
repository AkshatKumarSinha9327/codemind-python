n = int(input())
x = list(map(int,input().split()))
# print(x)
temp = []
for i in x:
    if i not in temp:
        print(i,end=' ')
        temp.append(i)