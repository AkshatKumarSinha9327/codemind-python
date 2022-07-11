n = int(input())
x = list(map(int,input().split()))

for i in x[::-1]:
    if i%2==1:
        print(i)
        break