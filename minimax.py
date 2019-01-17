from main import *

def minimax(board, player, depth):
  # returns best move (next board) for a player to make
  if depth == 0:
    return heuristic(board), board
  # for newBoard in getNextStates(board):
  newBoards = getNextStates(board, player)
  points = [minimax(newBoard, player * -1, depth -1)[0] for newBoard in newBoards]
  # print(points)
  if player == 1:
    return max(points), newBoards[points.index(max(points))]
  else:
    return min(points), newBoards[points.index(min(points))]

def bestmove(board, player, depth):
  _, nextBoard = minimax(board, player, depth)
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

# print(heuristic(board))
player = 1
for i in range(50):
  board = bestmove(board,player,3)
  print(i,player)
  print_board(board)
  player *= -1
  input()
    