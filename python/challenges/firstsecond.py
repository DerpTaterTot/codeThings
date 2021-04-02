import time
import random
import datetime  

def largestAndSecondLargest(lst):
    lst.sort(reverse = True)
    largest = lst[0]
    secondLargest = lst[1]
    return largest, secondLargest

def final(lst):
    if len(lst) > 1:
        oldlst = lst.copy()
        firstNumber, secondNumber = largestAndSecondLargest(lst)
        difference = oldlst.index(firstNumber) - oldlst.index(secondNumber)
        return abs(difference)
    else:
        return 0



def main():
    # using now() to get current time  
    current_time = datetime.datetime.now()
    print(current_time)

    lst =  [3, 25, 12, 11, 1,1,3,4,66,5,19]
    lst = [x for x in range(1000000)]
    random.shuffle(lst)
    start = time.time()

    print(final(lst))
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()
