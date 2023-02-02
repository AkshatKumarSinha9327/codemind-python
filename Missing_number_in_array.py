for _ in range(int(input())):
    n = int(input()) 
    x = list(map(int,input().split()))
    sumx = sum(x)
    sumn = int(n*(n+1)/2)
    print(sumn-sumx)