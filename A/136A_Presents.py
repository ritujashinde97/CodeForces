n = int(input())
k = input().split()

for i in range(n):
    print(k.index(str(i+1))+1)