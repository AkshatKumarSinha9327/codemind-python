n = int(input())
x = list(map(int,input().split()))
# print(x)
for i in x:
    if i!=1 and i!=0:
        print(False)
        break
else:
    print(True)