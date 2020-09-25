a = input()
b =input()
r = []
for i in range(len(a)):
    if a[i] != b[i]:
        r.append(1)
    elif a[i]==b[i]:
        r.append(0)
p = ''.join(map(str,r))
print(p)
 