def rev(n):
    temp = n
    rev = 0
    while temp:
        rev = rev*10 + temp%10
        temp//=10
    return rev

n = int(input())
x = list(map(int,input().split()))
nx = []
for i in x:
    nx.append(rev(i))
for i in nx:
    print(i,end=' ')