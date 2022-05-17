a = int(input())
b = int(input())
for i in range(a,b+1):
    temp = i
    rev=0
    while temp:
        rev = rev*10 + temp%10
        temp//=10
    if rev==i:
        print(i,end=' ')