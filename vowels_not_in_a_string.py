s = input()
temp = []
v = ['a','e','i','o','u']
for i in v:
    if i not in s:
        temp.append(i)
for i in sorted(temp):
    print(i,end=' ')
if not bool(len(temp)):
    print(0)