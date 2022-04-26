s = list(input())

for i in range(len(s)):
    if s[i].isupper():
        s[i] = s[i].lower()
        
    print(s[i],end='')