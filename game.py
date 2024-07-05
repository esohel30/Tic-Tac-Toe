board = ['_', '_', '_', 
         '_', '_', '_', 
         '_', '_', '_']

current_player = 'X'

def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

def play_turn(position):
    global current_player
    if board[position - 1] == '_': 
        board[position - 1] = current_player 
        if current_player == 'X':
            current_player = 'O'
        else: 
            current_player = 'X'
    else:
        print("Can't play that position. Go again Please.")

    display_board()

# neat algorithms needed
def check_win(): 
    for x in 


