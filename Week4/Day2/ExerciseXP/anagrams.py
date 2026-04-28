# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.
# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:

# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.

from anagram_checker import AnagramChecker
checker = AnagramChecker("sowpods.txt")
while True:
    print("\nMenu:")
    print("1. Input a word")
    print("2. Exit")
    choice = input("Choose: ")
    if choice == "2":
        print("Bye!")
        break
    elif choice == "1":
        user_input = input("Enter word: ")
        word = user_input.strip()
        if len(word.split()) > 1:
            print("Error: more than one word")
            continue
        if not word.isalpha():
            print("Error: only letters allowed")
            continue
        word = word.lower()
        print(f"\nYOUR WORD: {word.upper()}")
        if checker.is_valid_word(word):
            print("This is a valid English word.")
        else:
            print("This is NOT a valid English word.")
        
        anagrams = checker.get_anagrams(word)
        if anagrams: #not empty list (same - if len(anagrams) > 0:)
            print("Anagrams:", ", ".join(anagrams))
        else:
            print("No anagrams found.")
    else:
        print("Invalid choice")