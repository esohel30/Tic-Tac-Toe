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
    # check rows 
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] in ("X", "Y"):
            return True
    # check columns 
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] in ("X", "Y"):
            return True
    # check diagonals 
    if board[0] == board[4] == board[8] and board[0] in ("X", "Y"):
        return True 
    if board[2] == board[4] == board[6] and board[2] in ("X", "Y"):
        return True 
    
    return False
    

def play_game():
    while not check_win: 
        display_board()
        turn = int(input())
        
play_game()
    