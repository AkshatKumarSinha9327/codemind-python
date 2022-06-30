m,n = map(int,input().split())

x = list(map(int,input().split()))
y = list(map(int,input().split()))

# print(x,'
',y)
c=0
temp = []
for i in x:
    if (i in y) and (i not in temp):
        temp.append(i)
        c+=1
print(c)