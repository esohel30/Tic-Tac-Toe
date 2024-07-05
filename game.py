board = ['_', '_', '_', 
         '_', '_', '_', 
         '_', '_', '_']

def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

current_player = 'X'


def play_turn(position):
    if board[position - 1] == '_': 
        board[position - 1] = current_player 
    else: 
        print("Can't play that position. Go again Please.")
    
display_board()

play_turn(1)
play_turn(5)
play_turn(9)
play_turn(9)


display_board()

