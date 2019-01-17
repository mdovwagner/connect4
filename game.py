import copy
VISUALIZE = {0: " ", 1: "X", -1: "O"}
def make2DList(size):
    return [[0]*size for i in range(size)]

def connectedFour(L):
    count = 0
    for cell in L:
        if cell == 1:
            count +=1
            if count == 4:
                return 1
        else:
            count = 0
    return 0

def goodness(L):
    if len(L) < 4:
        return 0
    elif connectedFour(L):
        return 10000
    else:
        return sum(L)


def rowPoints(L, accumulateFn):
    maxiPoints = 0
    miniPoints = 0
    maxiPieces = []
    miniPieces = []
    for cell in L:
        if cell == 0:
            maxiPieces.append(0)
            miniPieces.append(0)
        elif cell == 1: # maxi
            if miniPieces != []:
                if sum(miniPieces) > 0:
                    miniPoints += accumulateFn(miniPieces)
                miniPieces = []
            maxiPieces.append(1)
        elif cell == -1: #mini
            if maxiPieces != []:
                if sum(maxiPieces) > 0:
                    maxiPoints += accumulateFn(maxiPieces)
                maxiPieces = []
            miniPieces.append(1)

    if sum(maxiPieces) > 0:
        maxiPoints += accumulateFn(maxiPieces)
    if sum(miniPieces) > 0:
        miniPoints += accumulateFn(miniPieces)
    return maxiPoints - miniPoints



def traverse(board, accumulateFn):
    points = 0
    n = len(board)
    for i in range(n):
        # rows
        row = board[i]
        points += rowPoints(row, accumulateFn)
        # cols
        col =[row[i] for row in board]
        points += rowPoints(col, accumulateFn)
        # main diagonals
        diag1  = [board[j][i+j] for j in range(n-i)]
        points += rowPoints(diag1, accumulateFn)
        if (i != 0):
            diag2  = [board[i+j][j] for j in range(n-i)]
            points += rowPoints(diag2, accumulateFn)
        # alt diagonal
        altdiag1 = [board[j][n-i-j-1] for j in range(n-i)]
        points += rowPoints(altdiag1, accumulateFn)
        if (i != 0):
            altdiag2 = [board[i+j][n-j-1] for j in range(n-i)]
            points += rowPoints(altdiag2, accumulateFn)
    return points


def heuristic(board):
    return traverse(board, goodness)

def won(board):
    if traverse(board,connectedFour) > 0:
        return 1
    elif traverse(board,connectedFour) < 0:
        return -1
    else:
        return 0

def getNextStates(board, player):
    boards =[]
    n = len(board)
    for i in range(n):
        newBoard = copy.deepcopy(board)
        legal = False
        for j in range(n-1,-1,-1):
            if newBoard[j][i] == 0:
                #empty space
                newBoard[j][i] = player
                legal =True
                break
        # print(newBoard)
        if (legal):
            boards.append(newBoard)
    return boards

def playmove(board, player, col):
    newBoard = copy.deepcopy(board)
    n = len(board)
    for row in range(n-1,-1,-1):
        if newBoard[row][col] == 0:
            #empty space
            newBoard[row][col] = player
            break
    return newBoard

def print_board(L):
    for row in L:
        print("\t[",end="")
        for col in row:
            print(VISUALIZE[col],end=",")
        print("]\n",end="")
    print("\t 1 2 3 4 5 6 7")


def print_boards(L):
    for board in L:
        print_board(board)





