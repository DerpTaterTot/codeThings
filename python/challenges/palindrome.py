def palindromeCheck(str):
    return str[::-1] == str

def main():
    word = 'aaaabbbaaaa'
    print(palindromeCheck(word))

if __name__ == "__main__":
    main()