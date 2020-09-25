n,k = map(int,input().split())
i = 0
while(i<k):
    i=i+1
    if((n%10)!= 0):
        n -=1
    elif((n%10)==0):
        n=n//10
        
print(n)
