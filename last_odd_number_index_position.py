a = int(input())
x = list(map(int,input().split()))
# print(x)
for i in range(len(x)-1,-1,-1):
    if x[i]%2==1:
        print(i)
        break