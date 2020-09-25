n = input()
count=0
for _ in n:
    a=n.count('4') 
    b=n.count('7')

if((a+b)==4 or (a+b)==7):
    print("YES")
else:
    print("NO")