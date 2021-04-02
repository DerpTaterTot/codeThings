def findUnique(string):
    for letter in string:
        if string.count(letter) == 1:
            return string.index(letter)
    return -1

print(findUnique('albert and anthony are good brothers for life'))

'''
def main():
    string = 'alphabet'
    print(findUnique(string))

main()

if __name__ == "__main__":
    main()
'''