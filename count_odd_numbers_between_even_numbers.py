n = int(input())
x = list(map(int,input().split()))
ini =0
inb = 0
for i in range(n):
    if x[i]%2==0:
        ini = i
        break
for i in range(n-1,-1,-1):
    if x[i]%2==0:
        inb = i
        break
c=0
for i in range(ini,inb):
    if x[i]%2==1:
        c+=1
print(c)