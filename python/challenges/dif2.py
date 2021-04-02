def dif(lst):
    high = -1e10
    low = 1e10
    for count in range(len(lst)):
        if lst[count] < low:
            low = lst[count]
        if lst[count] > high:
            high = lst[count]
    return high-low


def groups(Superlist, Length):
    lowestDifference = 1e10
    for i in range(len(Superlist) - Length + 1):
        d = dif(Superlist[i:i+Length])
        if d < lowestDifference:
            lowestDifference = d

    return lowestDifference



def main():
    lst = [6,3,5,4,6,7,5,6,54,56]
    print(groups(lst, 4))

if __name__ == "__main__":
    main()
