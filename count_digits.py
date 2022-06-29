n = int(input())
x= list(map(int,input().split()))

# print(x)
for i in x:
    if i<0:
        i*=-1
    print(len(list(str(i))),end=' ')