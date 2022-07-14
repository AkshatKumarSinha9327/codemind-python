s1 = input().lower().split()
s2 = input().lower().split()
temp = []
for i in s2:
    for j in s1:
        if i==j and i not in temp and s2.count(i)==1:
            temp.append(i)
            print(i,end=' ')