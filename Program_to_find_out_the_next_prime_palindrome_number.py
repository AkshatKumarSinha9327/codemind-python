def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def palin(n):
    temp = n
    rev = 0
    while temp:
        rev = rev*10 + temp%10
        temp//=10
    if rev==n:
        return True
    return False

n = int(input())
after = n+1
while after:
    if prime(after) and palin(after):
        print(after)
        break
    after+=1