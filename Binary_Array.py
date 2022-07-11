n = int(input())

x  = list(map(int,input().split()))

for i in x:
    if i not in [0,1]:
        print(False)
        break
else:
    print(True)