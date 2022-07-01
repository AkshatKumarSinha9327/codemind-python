def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


a,b = int(input()),int(input())
c=0
for i in range(1,100000000):
    if prime(a+b+i):
        print(i)
        break