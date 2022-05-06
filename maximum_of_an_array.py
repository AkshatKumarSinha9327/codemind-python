a = int(input())

x = list(map(int,input().split()))
max_ = x[0]
for i in range(len(x)):
    if max_<x[i]:
        max_=x[i]
print(max_)