import random
from os import system
digits = 4


def unique(s):
    return len(set(s)) == len(s)

def isInteger(string):
    return any(map(str.isdigit, string))

def random4digit2():
    lst = [x for x in range(10)]
    random.shuffle(lst)
    finalStr = ''
    for i in range(digits):
        finalStr += str(lst[i])
    return finalStr

def check(seed, guessed):
    cows = 0
    bulls = 0

    for i in range(len(guessed)):
        if guessed[i] == seed[i]:
            cows += 1 
        elif guessed[i] in seed:
            bulls += 1

    return cows, bulls


def cowsandbulls():
    guess = '10000'
    integer = random4digit2()
    tries = 0

    while guess != integer:
        guess = input('Guess an integer less than 10000(However, no two digits can be the same. 0 can also be the first digit): ')

        if unique(guess) == False:
            print('There are some duplicate digits')
            continue
        if len(guess) != digits:
            print('The guess does not have 4 digits (remember, 0 can be the first digit, but 0 cannot be used more than once)')
            continue
        if isInteger(guess) == False:
            print('The guess is not an integer')
            continue

        tries += 1
        cows,bulls = check(integer, guess)

        print('cows:', cows)
        print('bulls:', bulls)
    
    print('You win! The number was', integer, 'and it took you', tries, 'tries.')

if __name__ == "__main__":
    cowsandbulls()