# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
#wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    missing = [i for i in secretWord if i not in lettersGuessed]
    if len(missing) > 0:
        return False
    else:
        return True

#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(isWordGuessed(secretWord,lettersGuessed))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    outputWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            outputWord += letter
        else:
            outputWord += "_ "
    return outputWord
#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getGuessedWord(secretWord, lettersGuessed))
#'_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    outputString = ''
    import string
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            outputString += letter
    return outputString
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getAvailableLetters(lettersGuessed))
#abcdfghjlmnoqtuvwxyz    

def runGuess(countGuesses,lettersGuessed):
    '''
    countGuesses: int, number of guesses left to take
    lettersGuessed: list, letters already guessed, to lookup available letters
    
    Each time a guess is requested by hangman, this is run to
        accept input from the user, and make sure it's a viable entry
        
    Returns either the lower case letter, or false if entry is invalid
    '''
    print("-------------")
    print("You have "+str(countGuesses)+" left")
    print("Available letters: " + getAvailableLetters(lettersGuessed))                
    userGuess = input('Please guess a letter: ')
    if userGuess.isalpha():
        if len(userGuess) == 1:
            return userGuess.lower()
    return False
    
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
    lettersGuessed = []
    mistakesMade = 0
    countGuesses = 8    
    
    if len(lettersGuessed) == 0:
        print("Welcome to the game, Hangman!")
        print("I am thinking of a word that is "+str(len(secretWord))+" letters long")

    while countGuesses > 0:

        userGuess = runGuess(countGuesses,lettersGuessed)
        if userGuess == False:
            print("Please enter a single letter of the alphabet to guess")
        elif userGuess in lettersGuessed:
            outputWord = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter: " + outputWord)
        else:
            lettersGuessed.append(userGuess)
            outputWord = getGuessedWord(secretWord, lettersGuessed)
            if userGuess in secretWord:
                print("Good guess: " + outputWord)
                if isWordGuessed(secretWord,lettersGuessed):
                    print("-------------")
                    return print("Congratulations, you won!")
            else:
                countGuesses = countGuesses - 1
                print("Oops! That letter is not in my word: " + outputWord)
                mistakesMade += 1
    print ("-------------")
    return print("Sorry, you ran out of guesses. The word was " + secretWord)
    

hangman('tact')

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)
