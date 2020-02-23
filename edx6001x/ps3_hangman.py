# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
debug = False

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    ## if debug is True: print('line is type', type(line), 'and contains', line)
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if debug is True:
        print('entering isWordGuessed with secretWord', secretWord,
              'and lettersGuessed', lettersGuessed)
    gotit = True
    for letter in secretWord:
        if not letter in lettersGuessed:
            gotit = False
    return gotit



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if debug is True:
        print('entering getGuessedWord with secretWord', secretWord,
              'and lettersGuessed', lettersGuessed)
    guessedword = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            guessedword += secretWord[i]
        else:
            guessedword += '_'
    return guessedword



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    if debug is True:
        print('entering getAvailableLetters with lettersGuessed',
              lettersGuessed)
    allofem = list(string.ascii_lowercase)
    therestlist = list(string.ascii_lowercase)
    for letter in allofem:
        if letter in lettersGuessed:
            therestlist.remove(letter)
    thereststr = ''.join(therestlist)
    return thereststr
    
    
        
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    gotit = False
    guessesleft = 8
    lettersGuessed = []
    debug = False
    if debug is True: loopcount = 0
    while gotit == False and guessesleft > 0:
        if debug is True:
             print('entering main loop with loopcount', loopcount)
             loopcount += 1
        print('-------------')
        print('You have', guessesleft, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:",
                  getGuessedWord(secretWord, lettersGuessed))
            continue
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in my word:',
                  getGuessedWord(secretWord, lettersGuessed))
            guessesleft -= 1
        gotit = isWordGuessed(secretWord, lettersGuessed)
    print('------------')
    if gotit:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was', secretWord)
            

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
