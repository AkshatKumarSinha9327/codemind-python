
def lcm(a,b):
    m = max(a,b)
    while True:
        if m%a==0 and m%b==0:
            return m
        m+=max(a,b)

n = int(input())

x = list(map(int,input().split()))

ans = lcm(x[0],x[1])

for i in range(1,n):
    ans = lcm(ans,x[i])
print(ans)