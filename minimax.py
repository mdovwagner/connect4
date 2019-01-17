from game import *
DEBUG = 0
def dbg_print(s):
  if (DEBUG): print(s,end="")

def minimax(board, player, depth):
  # returns best move (next board) for a player to make
  if depth >= 4:
    return heuristic(board), board
  elif won(board):
    return -10000*player/(depth+1), board
  dbg_print("  "*depth + str(player)+"\n")
  newBoards = getNextStates(board, player)
  points = [minimax(newBoard, player * -1, depth +1)[0] for newBoard in newBoards]
  dbg_print("  "*depth + str(points)+"\n")
  # print(points)
  if player == 1:
    return max(points), newBoards[points.index(max(points))]
  else:
    return min(points), newBoards[points.index(min(points))]

def bestmove(board, player):
  dbg_print("~~~ MiniMax from player: "+str(player)+" ~~~\n")
  _, nextBoard = minimax(board, player, 0)
  return nextBoard


def parse_input(s):
  global DEBUG
  res = input(s)
  if res in "1234567" and len(res) == 1:
    return int(res) -1
  elif res == 'd':
    DEBUG = 1 - DEBUG
    print("Debug toggled")
  elif res == 'q':
    q = input("Press 'q' again if you're sure: ")
    if q == 'q':
      exit()
  else:
    print("Invalid character(s) entered")
  return parse_input(s)


# print(heuristic(board))
def play():
  player = 1
  n = 7
  board = [[0] * n for i in range(n)]
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("~~~ Welcome to Connect 4! ~~~")
  print("~~~ You will play as 'X's ~~~")
  print("~~~   I will play as 'O's ~~~")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("~~~   Pick a column 1-7   ~~~")
  print("~~~ Type 'd' to see debug ~~~")
  print("~~~ Type 'q' to quit game ~~~")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  for i in range(50):
    print("Turn: "+str(i//2+1)+", Player: "+VISUALIZE[player])
    if player == 1:
      col = parse_input("Type in a Column: ")
      board = playmove(board,player,col)
    else:
      board = bestmove(board,player)
    print_board(board)
    if (won(board)):
      print("Player: " + VISUALIZE[won(board)] + " wins!")
      break
    player *= -1
  