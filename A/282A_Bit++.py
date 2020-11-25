n = int(input())
x=0
for i in range(n):
    operation = input()
    x = x + (-1 if '-' in operation else 1)

print(x)