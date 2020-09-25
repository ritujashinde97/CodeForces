n = int(input())

ans = []

for _ in range(n):
    
    i = input()
    l = len(i)
    
    if l>10:
        ans.append(i[0] + str(l-2) + i[l-1])
    else:
        ans.append(i)
        
for b in ans:
    print(b)