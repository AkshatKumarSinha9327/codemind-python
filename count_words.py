s = input().lower().split()
v = 'aeiouAEIOU'
# print(s)
c= 0
for i in s:
    if i[0] in v and i[-1] not in v:
        c+=1
print(c)