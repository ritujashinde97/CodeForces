n = int(input())
i=0
r =''

for i in range(n):
    
    if(i%2!=0 ):
        r=r+'I love '
        if i==n-1:
            r=r+'it'
        else:
            r=r+'that '
    elif(i%2==0 ):
        r=r+'I hate '
        if i==n-1:
            r=r+'it'
        else:
            r=r+'that '
print(r)
            

        