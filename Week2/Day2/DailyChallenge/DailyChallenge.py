# You are given a “Matrix” string:
# MATRIX_STR = '''
# 7ir
# Tsi
# h%x
# i ?
# sM# 
# $a 
# #t%'''       
# This represents a grid of characters, and your task is to decode the hidden message within.

MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 

# Step 1: Convert matrix_string to a 2D list (matrix)
matrix = []
# ... code to create matrix ...
lines = MATRIX_STR.strip().split('\n') # We split the string by lines
for line in lines:
    matrix.append(list(line)) # We convert each line into a list of characters
# To iterate correctly, we need to know the number of rows and columns
num_rows = len(matrix)
num_cols = len(matrix[0])

# Step 2: Iterate through columns
# ... code to iterate through columns ...

# Step 3: Filter alpha characters
# ... code to filter alpha characters ...
# We read the grid vertically (column by column)
column_text = ""
for c in range(num_cols): # For each column index
    for r in range(num_rows): # Go through each row index
        char = matrix[r][c]
        # Collect every character in the order Neo reads them
        column_text += char

# Step 4: Replace symbols with spaces
# ... code to replace symbols with spaces ...
decoded_message = ""
i = 0
while i < len(column_text):
    if column_text[i].isalpha():
        # If it's a letter, just add it
        decoded_message += column_text[i]
        i += 1
    else:
        # If it's NOT a letter, check if there are letters both before and after this group
        # 1. Check if we already have some letters in our message (something is "before")
        # 2. Look ahead to see if there is any letter later in the string (something is "after")
        has_letter_after = False
        for j in range(i + 1, len(column_text)):
            if column_text[j].isalpha():
                has_letter_after = True
                break
        
        if decoded_message != "" and has_letter_after:
            # If we are between letters, add ONE space and skip all other symbols in this group
            decoded_message += " "
            # Move the index 'i' to the next letter
            while i < len(column_text) and not column_text[i].isalpha():
                i += 1
        else:
            # If it's symbols at the very beginning or end, just skip them
            i += 1

# Step 5: Print the decoded message
print(decoded_message)