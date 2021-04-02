def splitString(string):
    finalstr = ''
    string = string[::-1]

    split_strings = [string[index : index + 3] for index in range(0, len(string), 3)]
    
    #split_strings.reverse()

    for element in split_strings:
        #element = element[::-1]
        finalstr = finalstr + element + ','
        
    finalstr=finalstr[::-1]
    return finalstr[1:]

def splitStringv2(string = list):
    if '.' in string:
        finalStr = splitString(string.split('.')[0]) + '.' + string.split('.')[1]
        return finalStr
    else:
        return splitString(string)
    

print(splitStringv2('29124709183018209381209.1321238'))

print(splitStringv2('29124709183018209381209'))
