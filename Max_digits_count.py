n = int(input())

x = list(map(int,input().split()))

max_ = len(str(x[0]))
for i in x:
    if len(str(i))>max_:
        max_=len(str(i))

c = 0
for i in x:
    if max_==len(str(i)):
        c+=1
print(c)