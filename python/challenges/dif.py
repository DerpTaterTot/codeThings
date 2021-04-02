
def groups(Superlist, Length):
    allSubLists = []
    for i in range(len(Superlist) - Length + 1):
        tempList = []
        for count in range(Length):
            tempList.append(Superlist[i + count])
        allSubLists.append(tempList)    

    return allSubLists

def dif(lst):
    return max(lst) - min(lst)

def final(Superlist, Length):
    lowestDifference = dif(Superlist)
    difference = 0
    for sublist in groups(Superlist, Length):
        difference = dif(sublist)
        if difference < lowestDifference:
            lowestDifference = difference            

    return lowestDifference



def main():
    lst = [6,3,5,4,6,7,5,6,54,56]
    print(final(lst, 11))
    print(groups(lst, 11))

if __name__ == "__main__":
    main()
