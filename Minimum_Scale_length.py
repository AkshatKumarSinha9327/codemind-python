def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

n =int(input())

x= list(map(int,input().split()))

ans = gcd(x[0],x[1])

for i in range(1,n):
    ans = gcd(ans,x[i])
print(ans)