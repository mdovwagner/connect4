from main import *
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


board = [
 [ 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0],
 [ 1, 0, 1, 0, 0,-1, 0],
 [-1, 1,-1, 0, 1,-1, 0],
 [-1, 1, 1, 0, 1,-1, 0],
 [ 1, 1, 1, 0,-1, 1, 0],
 [ 1, 1, 1, 0,-1, 1, 0]
]

# board = [
#   [ 0, 0, 0, 0],
#   [ 0, 0, 0, 0],
#   [ 0,-1, 0, 0],
#   [ 1, 1, 0, 0]
# ]
n = 7
board = [[0] * n for i in range(n)]

def parse_input(s):
  global DEBUG
  res = input(s)
  if res in "1234567" and len(res) == 1:
    return int(res) -1
  elif res == 'd':
    DEBUG = 1 - DEBUG
    print("Debug toggled")
  else:
    print("Invalid characters entered")
  return parse_input(s)


# print(heuristic(board))
player = 1
for i in range(50):
  if player == 1:
    col = parse_input("Type in a Column: ")
    board = playmove(board,player,col)
  else:
    board = bestmove(board,player)
  print(i,VISUALIZE[player])
  print_board(board)
  if (won(board)):
    print("Player: " + VISUALIZE[won(board)] + " wins!")
    break
  player *= -1
  