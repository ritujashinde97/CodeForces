a = int(input())
count = 0

while (a>0):
    a -= 1
    k = input()
    if k.count('1') >= 2:
        count += 1
        
print(count)
        
    


                