n = int(input())

temp = n
sum_ =0 
while temp>0:
    sum_+=temp%10
    temp//=10
if n%sum_==0:
    print('True')
else:
    print('False')