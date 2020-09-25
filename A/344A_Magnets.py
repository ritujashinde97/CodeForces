n = int(input())
c = v = 0
for i in ' '*n:
	s = input()
	c += s != v
	v = s
 
print(c) 