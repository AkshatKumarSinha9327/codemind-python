a = int(input())

flag= 0
for i in range(1,a//2):
    if i*i == a:
        print('True')
        flag=1
        break
if flag!= 1:
    print('False')