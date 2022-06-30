m,n = map(int,input().split())

x = list(map(int,input().split()))
y = list(map(int,input().split()))

# print(x,'
',y)
temp = []
for i in x:
    if (i not in y) and (i not in temp):
        temp.append(i)
        print(i,end=' ')

for i in y:
    if (i not in x) and (i not in temp):
        temp.append(i)
        print(i,end=' ')