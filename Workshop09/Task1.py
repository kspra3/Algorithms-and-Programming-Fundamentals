# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

def FindFactorial(n):
    if n==0:
        return 1
    result = FindFactorial(n-1) * n
    aList.append(result)
    return result

aList=[]
FindFactorial(4)
print(aList)
