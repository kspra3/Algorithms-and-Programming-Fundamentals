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


num = int(input('Enter N: '))
partialSolution=[5,3]
positionRows = getPositions(partialSolution,num)
print(positionRows)
