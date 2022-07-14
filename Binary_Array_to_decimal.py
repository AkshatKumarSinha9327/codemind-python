n = int(input())
b = list(map(int,input().split()))
s = 0
for i in b:
    s+= i*(2**(n-1))
    n-=1
print(s)