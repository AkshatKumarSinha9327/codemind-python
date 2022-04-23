a,b = int(input()),int(input())
flag = 0
for i in range(a,b+1):
    temp = i;
    while(temp>0):
        a = temp%10
        if a!=0:
            if (i%a==0):
                flag =1;
            else:
                flag =0
                break
        else:
            flag=0
            break
        temp//=10
    if flag!=0:
        print(i,end=' ')