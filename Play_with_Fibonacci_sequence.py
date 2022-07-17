n = int(input())
a,b = 0,1
print(a,b,end=' ')
for i in range(n-2):
    print(a+b,end=' ')
    a,b = b,a+b