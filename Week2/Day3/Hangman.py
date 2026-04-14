# Mini-Project #2 - Hangman
# What you will learn
# Conditionals
# Loops
# Functions
# Modules
# What you will create
# Use python to create a Hangman game.
# Instructions
# The computer chooses a random word and marks stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.
# Starter code
# Here is a piece of code that will give you a random word.

#     import random

#     wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
#     word = random.choice(wordslist) 

#     ### YOUR CODE STARTS FROM HERE ###

import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) #we chose random word from the list wordlist

hangman_stages = [
    "",                     # 0
    "  O",                  # 1
    "  O\n  |",             # 2
    "  O\n /|",             # 3
    "  O\n /|\\",           # 4
    "  O\n /|\\\n /",       # 5
    "  O\n /|\\\n / \\"     # 6
]

hidden_word = [] #state of the word


for letter in word:
    if letter == ' ': #check if the symbol is space (e.g. in the word "hi you")
        hidden_word.append(' ')
    else:
        hidden_word.append('*') #we mark stars for each letter of each word, e.g. for credit card it will be ['*', '*', '*', '*', '*', '*', ' ', '*', '*', '*', '*']
        
def display_word(hidden_word):
    print(''.join(hidden_word)) #we display current state of the word nicely, e.g., "сredit card" → ****** ****


wrong_guesses = 0
max_wrong = 6
guessed_letters = []
while True:
    guess = input("Enter a letter: ")
    guess = guess.lower()
    if len(guess) != 1:
        print("Enter only ONE letter.")
        continue
    if not guess.isalpha():
        print("Enter a LETTER.")
        continue
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue
    guessed_letters.append(guess)
    if guess in word: #we check if the guess is in the word
        print("correct!")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        wrong_guesses += 1
        print("wrong!")
    display_word(hidden_word)
    print("Guessed letters:", guessed_letters)
    if '*' not in hidden_word:
        print("You win!")
        break
    print(hangman_stages[wrong_guesses])
    if wrong_guesses == max_wrong:
        print("You lost! The word was:", word)
        break
