#Name: Jaydeep zala
#Eno : 92600584080
#7. Implement Two Player Game - Tic-Tac-Toe (Using Heuristic Function).

#two player game - Tic-Tac-Toe
#using Heuristic Function

# Dispaly the board
def display(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print("--+---+--")
    print()

# Heuristic function
def heuristic(board):
    win =[
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in win:
        if board[a] == board[b] == board[c] == "X":
            return 10
        elif board[a] == board[b] == board[c] == "o":
            return -10

    return 0

# Main game
board = [" "] * 9
player = "X"

for turn in range(9):
    display(board)
    print("Player", player)

    position = int(input("Enter position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
         print("Invalid position! Try again.")
         continue

    board[position] = player

    # Check heuristic value
    score = heuristic(board)

    if score == 10:
        display(board)
        print("Player X wins!")
        break

    if score == -10:
        display(board)
        print("Player O wins!")
        break
    
    # change player
    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    display(board)
    print("Game Draw!")








    













        





        
