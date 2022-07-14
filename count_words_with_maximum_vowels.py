s = input().split()
v = 'aeiou'
mc = 0
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    if mc<c:
        mc = c
wc=0
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    if mc==c:
        wc+=1
print(wc)
