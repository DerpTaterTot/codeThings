def endZeroes(lst):
    x = 0
    finalList = [0] * len(lst)
    for number in lst:
        if number != 0:
            finalList[x] = number
            x += 1
    return finalList


print(endZeroes([1,7,0,0,8,0,6,6,3,4,6,7,0,0,2,5,7,0,10,12,0,4]))
