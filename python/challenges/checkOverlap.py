def checkOverlap(rect1, rect2):
    firstPointX, firstPointY, firstWidth, firstHeight = rect1
    secondPointX, secondPointY, secondWidth, secondHeight = rect2

    if firstPointX + firstWidth <= secondPointX:
        return False
    
    elif secondPointX + secondWidth <= firstPointX:
        return False
    
    elif firstPointY + firstHeight <= secondPointY:
        return False
    
    elif secondPointY + secondHeight <= firstPointX:
        return False

    return True


def areaOverlap(rect1, rect2):
    firstPointX, firstPointY, firstWidth, firstHeight = rect1
    secondPointX, secondPointY, secondWidth, secondHeight = rect2

    if checkOverlap(rect1, rect2) == False:
        return 0
    else:
        overlapX = min(firstPointX + firstWidth, secondPointX + secondWidth) - max(firstPointX, secondPointX)
        overlapY = min(firstPointY + firstHeight, secondPointY + secondHeight) - max(firstPointY, secondPointY) 
        return overlapX * overlapY

    #return max(0, min(firstPointX + firstWidth, secondPointX + secondWidth) - max(firstPointX, secondPointX))*max(0, min(firstPointY + firstHeight, secondPointY + secondHeight) - max(firstPointY, secondPointY))
        
rect1 = [0,1,2,3]
rect2 = [1,0,3,3]

print(areaOverlap(rect1, rect2))