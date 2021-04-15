# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

def printChessboard(T,n):
    chessboard= [[0] * n for i in range(n)]
    for i in range(len(chessboard)):
        col = i
        row = T[i]
        chessboard[row][col] = "Q"
    
    for i in range(len(chessboard)):
        output = ""
        for j in range(len(chessboard[i])):
            output+=str(chessboard[i][j]) + " "
        print(output)

        
def getPositions(T,n): 
    rows = []
    for i in range(n):
        T.append(i)
        if checkSolution(T)==True:
            rows.append(i)
        T.pop()
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

def nQueens(partialSolution,n,sCount=0):
    if len(partialSolution) == n:
        sCount +=1
        printChessboard(partialSolution,n)
        print('----------------------')
    else:
        positions = getPositions(partialSolution,n)
        for i in range (len(positions)):
            partialSolution.append(positions[i])
            sCount = nQueens(partialSolution,n,sCount) 
            partialSolution.pop()
    return sCount


num = int(input('Enter value for n: '))

print('--------------')
nSolutions = nQueens([],num)
if nSolutions != 0:
    print('There are %d solutions.' % nSolutions)
else:
    print('There are no solutions.')
