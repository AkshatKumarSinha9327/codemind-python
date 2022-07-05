s=list(set(input().lower()))
#s.remove(' ')
s.sort()
for i in s:
    if i!=' ':
        print(i,end='')