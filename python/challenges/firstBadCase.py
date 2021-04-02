#import math
import random

N=1000
bad = random.randint(1,N)
cost = 0

def isBadVersion(v):
    global cost
    global bad
    cost += 1000
    return (v>=bad)   

def firstBadCase(N):
    left = 1
    right = N

    while left < right:
        middle = left + (right - left) // 2
        if isBadVersion(middle):
            right = middle
        else:
            left = middle + 1
    return left

print(firstBadCase(1000))
print('actual bad is: ', bad)
print(cost)


'''
    while True:
        n = start + end // 2 
        if isBadVersion(n) and isBadVersion(n - 1) == False:
            return n
        elif isBadVersion(n - 1):
            end = n - 1
        else:
            start = n + 1
'''