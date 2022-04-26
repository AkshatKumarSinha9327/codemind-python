t = int(input())
for i in range(t):
    flag =0
    num = ['0','1','2','3','4','5','6','7','8','9']
    s = input()
    for j in num:
        if j in s:
            flag=1
            break
        else:
            flag=0
    if flag==1:
        print('Yes')
    else:
        print('No')