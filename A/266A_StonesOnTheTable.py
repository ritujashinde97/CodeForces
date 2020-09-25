def solve(n,stones):
    count = 0
    for i in range(1,n):
        if(stones[i]==stones[i-1]):
            count += 1
            
    return count
    
n = int(input())
stones = input()
r = solve(n,stones)
print(r)
            