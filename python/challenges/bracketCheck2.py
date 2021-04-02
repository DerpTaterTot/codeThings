def checkParenthesis(string):
    brackets = ['[]', '{}', '()']
    while '[]' in string or '{}' in string or '()' in string:
        for br in brackets: 
            string = string.replace(br, '')
    
    return not string

parenthesis = "{[]{()}}"

print(checkParenthesis(parenthesis))