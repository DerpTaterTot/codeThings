import time
def rotate(lst, k):
    steps = k
    currentList = lst.copy()
    for i in range(len(lst)):
        rotated = i + steps
        rotated = rotated % len(lst)
        if rotated > len(lst) - 1:
            index = rotated - len(lst)
            currentList[index] = lst[i]
        else:
            currentList[rotated] = lst[i]

    return currentList

def rotate2(lst, k):
    l=len(lst)
    k  = k%l
    return lst[l-k:]+lst[0:l-k]

start = time.time()
print(rotate2([1,2,3,4,5,6,7], 100000000000000000000))
end = time.time()
print(end - start)

