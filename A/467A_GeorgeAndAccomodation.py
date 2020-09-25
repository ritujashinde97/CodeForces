n = int(input())
count=0
i=0
while(i<n):
    i +=1
    p,q =map(int,input().split())
    a = q-p
    if (a >=2):
        count+=1
print(count)
