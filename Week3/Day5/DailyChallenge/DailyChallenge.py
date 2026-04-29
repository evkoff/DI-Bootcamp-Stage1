# Text analysis
# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# OOP (Classes, Class Methods, Inheritance)
# Modules (File Handling, String Manipulation, Data Structures)
# Text Analysis Techniques
# Key Python Topics:
# OOP (Classes, Class Methods, Inheritance)
# File handling (open())
# String manipulation (split(), join(), translate(), regular expressions)
# Dictionaries
# Sets
# Lists
# string module
# re module (regular expressions)
# Instructions:
# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.
# Part I: Analyzing a Simple String
# Step 1: Create the Text Class
# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).
import string
import re

class Text:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Text must be a string")
        self.text = text
# Step 2: Implement word_frequency Method
# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.
    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        if count == 0:
            return None
        return count 

# Step 3: Implement most_common_word Method
# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.
    def most_common_word(self):
        words = self.text.lower().split()
        freq = {}
        
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        most_common = max(freq, key=lambda x: freq[x])
        return most_common

# Step 4: Implement unique_words Method
# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.
    def unique_words(self):
        words = self.text.lower().split()
        unique = set(words)
        return list(unique)

# Part II: Analyzing Text from a File
# Step 5: Implement from_file Class Method
# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return cls(content)
# Bonus: Text Modification
# Step 6: Create the TextModification Class
# Create a class called TextModification that inherits from Text.

class TextModification(Text):
# Step 7: Implement remove_punctuation Method
# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.
    def remove_punctuation(self):
        translator = str.maketrans("", "", string.punctuation)
        cleaned_text = self.text.translate(translator)
        return cleaned_text 
# Step 8: Implement remove_stop_words Method
# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.
    def remove_stop_words(self):
        stop_words = {"a", "the", "is", "in", "on", "and"}
        clean_text = self.remove_punctuation()
        words = clean_text.lower().split()
        filtered_words = [word for word in words if word not in stop_words]
        return " ".join(filtered_words)    
# Step 9: Implement remove_special_characters Method
# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.
    def remove_special_characters(self):
        cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", self.text) #re.sub(pattern, replacement, text), ^ means NOT, \s means any space-like symbol (" ", \n, \t (tab))
        return cleaned


t = TextModification("Hello, hello! This is a test.")
print(t.remove_stop_words())