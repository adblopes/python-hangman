import urllib.request
import random
from os import system, name

contents = urllib.request.urlopen("https://www.mit.edu/~ecprice/wordlist.10000").read()
contents = contents.split()
wordList = []
letters = []
lives = 5
win = False
word = ""
revealedWord = []

for i in contents:
    if len(i) > 4:
        wordList.append(i)

def main():
    print("Welcome to Hangman! I'm going to come up with a word and you'll have to guess it, I'll give you 5 lives.")
    
    try:
        while(True):
            input("Press ENTER to continue")
            start()
    except KeyboardInterrupt:
        print("Program terminated by user. Exiting...")

def hangman():
    global lives, win, letters, revealedWord, word

    clear()
    drawFrame()
    
    if (lives > 0 and win == False):
        userGuess = input("What's your guess? ")
        
        while (len(userGuess) > 1 or not userGuess.isalpha() or userGuess in letters):     
            if (len(userGuess) > 1 or not userGuess.isalpha()):
                print("Hey! That's not a valid guess! I only accept single letters")
            if (userGuess in letters):
                print(f"You've already guessed {userGuess}, try something else.")
            
            userGuess = input("What's your guess? ")

        letters.append(userGuess.lower())

        if userGuess in word:
            for i in range(0, len(word)):
                if userGuess == word[i]:
                    revealedWord[i] = userGuess
            
            if ''.join(revealedWord) == word:
                win = True
        else:
            lives -= 1

        hangman()
    
    if win:
        input("\nYou got it! Congrats! How about another game? Press ENTER to play again!")
        start()
    
    if lives == 0:
        input("\nAww you lose, wanna play again? Press ENTER to play another game!")
        start()

def start():
    global wordList, lives, win, word, revealedWord

    clear()
    word = str(wordList[random.randint(0, len(wordList)-1)]).strip("b'")
    lives = 5
    win = False
    letters.clear()
    revealedWord.clear()

    for i in word:
        revealedWord.append("_")

    hangman()

def clear():
    system("cls") if name == "nt" else system("clear")

def drawFrame():
    global lives, wordList, letters, revealedWord
    printLetters = ", ".join(letters)

    print("Let's go!\n")
    print("        ________")
    print("        |      |")

    if lives < 5:
        print("       _|_     |")
        print("      /   \    |")
        print("      \___/    |")
    else:
        print("        |      |")    
        print("               |")    
        print("               |")   

    if lives < 4:
        print("        |      |")
        if lives < 3:            
            print("       /|\     |")
        else:
            print("       /|      |")
    else:
        print("               |")    
        print("               |")  

    if lives < 2:
        print("        |      |")
        if lives < 1:   
            print("       / \     |")
        else:
            print("       /       |")
    else:
        print("               |")    
        print("               |")  

    print("               |")
    print("      _________|_____")
    print("")
    print(f"{len(revealedWord)}-Letter Word:", word if lives == 0 else ''.join(revealedWord))
    print("")
    print(f"Lives: {lives}" + f" | Guesses: {printLetters}")    
    
main()