import math
x = list(map(float , input().split()))
a = x[0]
b = x[1]
c = x[2]

s = (a + b + c)/2

area = math.sqrt( s * ( ( s - a ) * ( s - b ) * ( s - c)))

print('{:.2f}'.format(area))