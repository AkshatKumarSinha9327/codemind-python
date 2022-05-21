def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

a = int(input())

if prime(a):
    rev = 0
    while a:
        rev = rev*10 +a%10
        a//=10
    if prime(rev):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')