# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

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

def nQueens(partialSolution,n):
    if len(partialSolution) == n:
        print(partialSolution)
    else: 
        positions = getPositions(partialSolution,n)
        for i in range (len(positions)):
            partialSolution.append(positions[i])
            nQueens(partialSolution,n)
            partialSolution.pop()

num = int(input('Enter value for n: '))
print('Solutions')
print('--------------')
nQueens([],num)
print('--------------')        
