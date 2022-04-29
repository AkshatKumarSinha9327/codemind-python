a = int(input())

while 1:
    temp =a
    sum_=0
    dcount =0
    while temp>0:
        sum_ += (temp%10)**2
        dcount+=1
        temp//=10
    if dcount==1:
        if sum_==1:
            print(True)
            break
        else:
            print(False)
            break
    else:
        a = sum_