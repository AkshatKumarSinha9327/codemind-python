hurlf,spinf,speedf = map(int,input().split())

grade = 0
if(hurlf>50 and speedf>100 and spinf>60):
    grade = 10
elif(hurlf>50 and spinf>60):
    grade = 9
elif(speedf>100 and spinf>60):
    grade = 8
elif(hurlf>50 and speedf>100):
    grade = 7
elif (hurlf>50 or speedf>100 or spinf>60):
    grade = 6
else:
    grade = 5
print(grade)