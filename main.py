import copy
VISUALIZE = {0: " ", 1: "X", -1: "O"}
def make2DList(size):
    return [[0]*size for i in range(size)]


def won(board):
    rows = len(board)
    for row in range(rows):
        for col in range(rows):
            # horizontle
            total = 0
            for i in range(4):
                try:
                    total += board[row][col+i]
                except:
                    total += 0
            if total == 4:
                return 1
            if total == -4:
                return -1
            # veritcal
            total = 0
            for i in range(4):
                try:
                    total += board[row+i][col]
                except:
                    total += 0
            if total == 4:
                return 1
            if total == -4:
                return -1
            # diagonal
            total = 0
            for i in range(4):
                try:
                    total += board[row+i][col+i]
                except:
                    total += 0
            if total == 4:
                return 1
            if total == -4:
                return -1
            # diagonal 2
            total = 0
            for i in range(4):
                try:
                    total += board[row+i][col-i]
                except:
                    total += 0
            if total == 4:
                return 1
            if total == -4:
                return -1



def groupPoints(L):
    if len(L) < 4:
        return 0
    elif sum(L) == 4:
        return 10000
    else:
        return sum(L)

def rowPoints(L):
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
                    miniPoints += groupPoints(miniPieces)
                miniPieces = []
            maxiPieces.append(1)
        elif cell == -1: #mini
            if maxiPieces != []:
                if sum(maxiPieces) > 0:
                    maxiPoints += groupPoints(maxiPieces)
                maxiPieces = []
            miniPieces.append(1)

    if sum(maxiPieces) > 0:
        maxiPoints += groupPoints(maxiPieces)
    if sum(miniPieces) > 0:
        miniPoints += groupPoints(miniPieces)
    return (maxiPoints, miniPoints)



def heuristic(board):
    maxiPoints = 0
    miniPoints = 0
    # if won(board) != 0:
    #     return won(board) * 10

    n = len(board)
    # rows
    for i in range(n):
        row = board[i]
        (mA, mI) = rowPoints(row)
        maxiPoints += mA
        miniPoints += mI
    # cols
    for i in range(n):
        col =[row[i] for row in board]
        (mA, mI) = rowPoints(col)
        maxiPoints += mA
        miniPoints += mI
    # main diagonals
    for i in range(n):
        diag1  = [board[j][i+j] for j in range(n-i)]
        (mA, mI) = rowPoints(diag1)
        maxiPoints += mA
        miniPoints += mI
        if (i != 0):
            diag2  = [board[i+j][j] for j in range(n-i)]
            (mA, mI) = rowPoints(diag2)
            maxiPoints += mA
            miniPoints += mI
    # alt diagonal
    for i in range(n):
        diag1 = [board[j][n-i-j-1] for j in range(n-i)]
        (mA, mI) = rowPoints(diag1)
        maxiPoints += mA
        miniPoints += mI
        if (i != 0):
            diag2 = [board[i+j][n-j-1] for j in range(n-i)]
            (mA, mI) = rowPoints(diag2)
            maxiPoints += mA
            miniPoints += mI

    return maxiPoints - miniPoints

            # while True:


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





