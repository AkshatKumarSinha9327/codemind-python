a = int(input())

x = list(map(int,input().split()))
min_ = x[0]
for i in range(len(x)):
    if min_>x[i]:
        min_=x[i]
print(min_)