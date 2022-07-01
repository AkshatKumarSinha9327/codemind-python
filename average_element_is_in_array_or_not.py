n = int(input())

x = list(map(int,input().split()))

avg = int(sum(x)/n)
print(avg in x)