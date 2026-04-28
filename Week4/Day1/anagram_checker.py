# Mini-project : Anagram checker
# Last Updated: February 19th, 2025
# What you will learn
# OOP
# Python Files I/O
# What you will create
# 🌟 Anagram checker
# We will create a program that will ask the user for a word.
# It will check if the word is a valid English word, and then find all possible anagrams for that word.
# Instructions
# First Download this text file
# Create a new file called anagram_checker.py which contains a class called AnagramChecker.
# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# 
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.
# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)
# Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.
# Note: None of the methods in the class should print anything.


class AnagramChecker:
    def __init__(self, word_list_file):
      # Load all words from file into a list
        with open(word_list_file, "r") as f:
            # convert ALL words to lowercase
            #self.words = [word.strip().lower() for word in f.readlines()]
            self.words = {word.strip().lower() for word in f}
    def is_valid_word(self, word):
        #should check if the given word (ie. the word of the user) is a valid word (exists in the dictionary)
        return word.lower() in self.words
    def is_anagram(self, word1, word2):
        #will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.
        return sorted(word1) == sorted(word2) and word1 != word2
    def get_anagrams(self, word):
        #should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)
            word = word.lower()
            # Find all words that are anagrams
            anagrams = [
                w for w in self.words
                if self.is_anagram(word, w)
            ]
            return anagrams
   