s1 = input().lower()
s2 = input().lower()
c=0

for i in s2:
    if i not in s1:
        c=0
        break
else:
    c=1

if c==1:
    for i in s1:
        if i not in s2:
            c=0
            print(False)
            break
    else:
        print(True)
else:
    print(False)