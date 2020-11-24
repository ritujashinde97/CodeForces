s = int(input())
no_of_pass = 0
capacity = 0
for i in range(s):
    ex, en = map(int, input().split())
    no_of_pass -= ex
    no_of_pass += en
    capacity = max(capacity, no_of_pass)
print(capacity)