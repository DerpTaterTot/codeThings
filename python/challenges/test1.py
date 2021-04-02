def subcheck(bigList, smallList):
    for a in range(len(smallList)):
        for b in range(len(bigList)):
            try:
                if bigList[b] == smallList[a]:
                    smallList.pop(a)
            except:
                pass
    return not smallList

print(subcheck([4,5,7], [4]))

