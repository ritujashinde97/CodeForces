a = int(input())

p = [5,4,3,2,1]
count = 0
while(a>0):

    for q in p:
        if(a>=q):
            count+=1
            a-=q
            break

print(count)
            
    
    

