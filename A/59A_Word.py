s = input()
lower=0
upper=0
for i in s:
    if (i>='a' and i<='z'):
        lower+=1
    elif( i >= 'A' and i<='Z'):
        upper+=1
        
if(lower>upper):
    print(s.lower())
elif(lower<upper):
    print(s.upper())
elif(lower==upper):
    print(s.lower())
