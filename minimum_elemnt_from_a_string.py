s = input().split()
mn = min(s[-1])
if mn.lower() in s[-1]:
    print(mn.lower())
else:
    print(min(s[-1]))