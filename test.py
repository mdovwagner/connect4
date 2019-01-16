from main import *
def test_heuristic(board, ans):
    if heuristic(board) != ans:
        print(heuristic(board),"!=",ans)

board = [
 [ 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0],
 [ 1, 0, 1, 0, 0,-1, 0],
 [-1, 1,-1, 0, 1,-1, 0],
 [-1, 1, 1, 0, 1,-1, 0],
 [ 1, 1, 1, 0,-1, 1, 0],
 [ 1, 1, 1, 0,-1, 1, 0]
]

print(heuristic(board))


def test_points(L, ans):
    if(rowPoints(L) != ans):
        print(rowPoints(L),"!=",ans)



L = [1,-1,1,1,0,-1,-1,0,-1,-1,1,-1,0,-1,-1]
test_points(L, (0, 17))
L = [0, 0, 0, 1, 0, 0, 0]
test_points(L, (8, 0))
L = [1, 1, -1, 0, 0, 0, 1]
test_points(L, (5, 5))
L = [-1, 0, 1, -1, -1, 0, 1]
test_points(L, (0, 0))
L = [-1, 0, 1, -1, -1, 0, -1]
test_points(L, (0, 7))
L = [0, 1, 1, 0, 1, -1, 0]
test_points(L, (8, 0))
