s = input().lower()
temp = []
for i in sorted(s):
    if s.count(i)==1 and i not in temp and i!=' ':
        print(i,end='')