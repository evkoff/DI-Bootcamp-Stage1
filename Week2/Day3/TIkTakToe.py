# Goal: Create a Tic Tac Toe game in Python where two players can play against each other.
# Step 1: Representing the Game Board
# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).
board = [
    [' ', ' ', ' '], # row 0
    [' ', ' ', ' '], # row 1
    [' ', ' ', ' ']  # row 2
]
# Step 2: Displaying the Game Board
# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.
def display_board(board):
    print(board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('---------')
    print(board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('---------')
    print(board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
display_board(board)
# Step 3: Getting Player Input
# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.

def player_input(board, player):
    while True: #“Repeat forever until I explicitly stop”
        # Ask user for row and column
        row_input = input("Player " + player + ", enter row (0-2): ")
        
        # check if input is a number
        if not row_input.isdigit():
            print("Please enter numbers only.")
            continue

        # convert to int
        row = int(row_input)
        
        if row < 0 or row > 2:
            print("Row out of range.")
            continue

        col_input = input("Player " + player + ", enter col (0-2): ")
        if not col_input.isdigit():
            print("Please enter numbers only.")
            continue
        col = int(col_input)


         #  check range
        if col < 0 or col > 2:
            print("Out of range. Try again.")
            continue
        
        # Check if the cell is empty
        if board[row][col] == ' ':
            return row, col #return exits the loop and the function
        else:
            print("This cell is already taken. Try again.")

# Step 4: Checking for a Winner

# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.

def check_win(board, player):
    # Check rows
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
   
   # Check columns
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False #“We checked everything… and NO, the player did NOT win”

# Step 5: Checking for a Tie
# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.
# This function checks if the board is full
def check_tie(board):
    # If any cell is still empty → not a tie
    if board[0][0] == ' ' or board[0][1] == ' ' or board[0][2] == ' ':
        return False
    if board[1][0] == ' ' or board[1][1] == ' ' or board[1][2] == ' ':
        return False
    if board[2][0] == ' ' or board[2][1] == ' ' or board[2][2] == ' ':
        return False
    
    return True #“We checked everything… and YES, it IS a tie”

# Step 6: The Main Game Loop
# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).

def play():
    # Create a new empty board
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    # First player
    current_player = 'X'

    while True:
        # Show board
        display_board(board)

        # Get move
        row, col = player_input(board, current_player)

        # Place symbol
        board[row][col] = current_player

        # Check win
        if check_win(board, current_player):
            display_board(board)
            print("Player " + current_player + " wins!")
            break

        # Check tie
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

play()