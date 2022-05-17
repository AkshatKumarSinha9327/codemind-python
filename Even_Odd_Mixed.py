a=int(input())

l = len(str(a))
ocount=0
ecount=0

while a:
    b = a%10
    a//=10
    if b%2==0:
        ecount+=1
    else:
        ocount+=1
if ecount==l:
    print('Even')
elif ocount==l:
    print('Odd')
else:
    print('Mixed')