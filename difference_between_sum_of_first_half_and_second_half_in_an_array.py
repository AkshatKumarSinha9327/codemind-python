n = int(input())

x = list(map(int,input().split()))

s,sx = sum(x[:n//2]),sum(x[n//2:])

print(abs(s-sx))