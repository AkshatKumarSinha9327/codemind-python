n = int(input())
x = list(set(map(int,input().split())))
s=0
for i in x:
    if i%2==0 and x.count(i)==1:
        s+=i
        
print(s)