def ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return ways(n-1) + ways(n-2)

def betterWays(n):
    ways=[1]*n
    ways[1]=2
    for i in range(2,n):
        ways[i]=ways[i-1]+ways[i-2]
    return ways[-1]

print(betterWays(50))