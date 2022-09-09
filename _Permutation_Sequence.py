from itertools import permutations

n,m = map(int,input().split())
x = list(permutations(range(1,n+1)))
for i in x[m-1]:
    print(i,end='')