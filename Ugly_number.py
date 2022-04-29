def prime(n):
    factor =0
    for i in range(1,n+1):
        if n%i==0:
            factor+=1
    if (factor ==2):
        return True
    else:
        return False
        
a = int (input())
prime1=[]
for i in range(1,a+1):
    if a%i==0 and prime(i):
        prime1.append(i)
if (2 in prime1 or 3 in prime1 or 5 in prime1 ):
    print("Ugly Number")
elif a==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")