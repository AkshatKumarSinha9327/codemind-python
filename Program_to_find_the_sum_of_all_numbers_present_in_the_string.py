s = input()
sum_ = 0
for i in s:
    if i<='9' and i>= '0':
        sum_+= int(i)
print(sum_)