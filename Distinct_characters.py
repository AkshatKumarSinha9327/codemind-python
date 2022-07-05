s = list(input().lower())
l = []
for i in s:
    if s.count(i)==1 and i!=' ':
        l.append(i)
l.sort()
for i in l:
    print(i,end= '')