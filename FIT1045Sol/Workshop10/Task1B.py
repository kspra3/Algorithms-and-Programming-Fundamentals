# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

def printChessboard(T):
    for i in range(len(T)):
        output = ""
        for j in range(len(T[i])):
            output+=str(T[i][j]) + " "
        print(output)
        
def getPositions(T,n): 
    chessboard= [[0] * n for i in range(n)]
    for i in range(len(T)):
        col = i
        row = T[col]
        chessboard[row][col] = 'Q'

    rows = []
    nextCol =  len(T)
    
    for i in range(n):
        T.append(i)
        if checkSolution(T)==True:
            rows.append(i)
            chessboard[i][nextCol]='X'
        T.pop()

    printChessboard(chessboard)

    return rows

def checkSolution(T):
    return (checkRow(T) and checkColumn(T) and checkDiagonal(T))

def checkRow(T):
    for i in range(len(T)):
        for c in range(i + 1 ,len(T)):
            if T[i] == T[c]:  
                return False
    return True
 
def checkColumn(T):
    for i in range(len(T)):
        if T[i] == '':   
            return False
    return True
 
def checkDiagonal(T):
    for i in range(len(T) - 1):
        if abs(T[i] - T[i + 1]) == 1:
            return False
    return True


num = int(input('Enter N: '))
partialSolution=[5,3]
getPositions(partialSolution,num)
