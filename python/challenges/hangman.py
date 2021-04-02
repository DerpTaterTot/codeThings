import random
from os import system
fpath = '/home/albertchen/works/pythonworks/challenges/sowpods.txt'

def randomword(filepath):
    with open(filepath) as lst:
        word = random.choice(lst.read().splitlines())    
        
    return word

hangmans = [''' 
            -------------------
            |         O
            |
            |
            |
            |
            |
            |
            |
            ''',
            ''' 
            -------------------
            |         O
            |         |
            |         |
            |
            |
            |
            |
            |
            ''' ,
            ''' 
            -------------------
            |         O
            |        /|
            |         |
            |
            |
            |
            |
            |
            ''' ,
            ''' 
            -------------------
            |         O
            |        /|\\
            |         |
            |
            |
            |
            |
            |
            ''' ,
            ''' 
            -------------------
            |         O
            |        /|\\
            |         |
            |        /
            |
            |
            |
            |
            ''' ,
            ''' 
            -------------------
            |         O
            |        /|\\
            |         |
            |        / \\
            |
            |
            |
            |
            '''
            ]

def guessWord(word):
    guessedList = []
    word = word.upper()
    string = ''
    loseCounter = 0
    for _ in word:
        string = string + '_ '
    while loseCounter < 5:
        guess = input('guess letter: ')
        if not guess:
            continue
        guess = guess[0].upper()
        if guess in guessedList:
            print('you have already guessed this letter!')
            continue
        guessedList.append(guess)
        base = 0
        for i in range(0, len(word)):
            if guess ==  word[i]:
                base += 1                
                string_list = list(string)
                string_list[2*i] = guess
                string = "".join(string_list)
        
        if base == 0:
            loseCounter += 1
        
        system('clear')
        print(hangmans[loseCounter])
        print(string)
        print('')
        print('You have', 5 - loseCounter, 'tries left and have chosen these letters:', guessedList)


        if string.replace(' ', '') == word:
            print(string)
            return 'You Win! The word was', word

    return 'you lose, the word was', word


def main():
    
    tryagain = 0
    while tryagain == 0:
        random = randomword(fpath)
        print(guessWord(random))
        correct = 0
        while correct != 1:
            again = input('would you like to play again? ')
            if not again:
                print('did not get a valid answer, try again')
            if again[0].upper() == 'N':
                tryagain += 1
                correct += 1
                print('have a good day!') 
            else:
                correct += 1
                system('clear')


if __name__ == '__main__':
    main()


