I=lambda:map(int,input().split())
n,h=I()
print(n+sum([i>h for i in I()]))