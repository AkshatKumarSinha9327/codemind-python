a = int(input())

temp =a
dcount=0
while temp>0:
    dcount+=1
    temp//=10
sum_=0
temp=a
while temp>0:
    # print(sum_,'+=',temp%10,'**',dcount);
    sum_+= (temp%10) ** dcount
    dcount-=1
    temp//=10
print(sum_==a)