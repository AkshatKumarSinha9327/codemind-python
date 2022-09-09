for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(0,max(a,b)):
        if (i*i)%b==a:
            print(i)
            break
    else:
        print(-1)