k, n, w = map(int, input().split(" "))
cost = 0

for i in range(w):
    cost = cost + (i+1)*k

if(cost - n > 0):
    print(cost-n)
else:
    print(0)