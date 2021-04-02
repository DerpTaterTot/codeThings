import random

def check(lst):
    count = 0
    for i in range(len(lst)):
        for ii in range(i + 1, len(lst)):
            for j in range(ii + 1, len(lst)):
                if lst[i] + lst[ii] + lst[j] == 0:
                    print([lst[i], lst[ii], lst[j]])
                    count += 1
                    break

    print(count)
                    



a = [x for x in range(-10, 11)]
random.shuffle(a)

check(a)
