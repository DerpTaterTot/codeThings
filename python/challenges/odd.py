import random
import time

def odd(lst):
    finalList = []
    usedNumbers = []
    for i in range(len(lst)):
        if lst[i] in usedNumbers:
            continue
        usedNumbers.append(lst[i])
        count = 1
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                count += 1
        if count % 2 == 1:
            finalList.append(lst[i])
            

    return finalList

lst = [3, 4, 6, 7, 4, 7, 7, 3, 4, 6, 6, 8, 8, 7]
print(odd(lst))

a=[random.randint(1,100)  for _ in range(3000000)]
start = time.time()
r=odd(a)
end = time.time()
r.sort()
print(r)
print('used time: ', end-start)



def odd2(lst):
    count =[0]*101
    r=[]
    for x in lst:
        count[x]+=1
    for i in range(101):
        if count[i]%2 == 1:
            r.append(i)
    return r

start = time.time()
r2=odd2(a)
end= time.time()
r2.sort()
print(r2)
print('method2 time: ',end-start)