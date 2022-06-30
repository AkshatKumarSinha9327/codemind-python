n = int(input())

x = list(map(int,input().split()))

min_ = len(str(x[0]))
for i in x:
    if len(str(i))<min_:
        min_=len(str(i))

c = 0
for i in x:
    if min_==len(str(i)):
        c+=1
print(c)