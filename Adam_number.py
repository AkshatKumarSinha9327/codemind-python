a = int(input())

a_sq = list(str(a*a))
temp = a
rev =0
while temp>0:
    rev = rev*10 + temp%10
    # print(rev)
    temp//=10
rev_sq = list(str(rev*rev))
rev_sq.reverse()
print(a_sq==rev_sq)