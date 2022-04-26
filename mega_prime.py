a = int(input())
factor =0
for i in range(1,a+1):
    if a%i==0:
        factor+=1

if factor==2:
    temp = a
    flag=0
    while temp>0:
        check = temp%10
        if check==5 or check ==3:
            flag=1
        else:
            flag=0
            break
        temp//=10
    if flag==1:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
    
else:
    print("Not Mega Prime")