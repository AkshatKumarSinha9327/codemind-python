def perfect(num):
    for i in range(1,num):
        if i*i==num:
            return True
    return False
    
t = int(input())

for i in range(t):
    print(perfect(int(input())))