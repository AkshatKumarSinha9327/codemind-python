s=list(input().lower())
l=[]
for i in s:
    if s.count(i)==1 and i!=" ":
        print(i)
        break
else:
    print(-1)
    