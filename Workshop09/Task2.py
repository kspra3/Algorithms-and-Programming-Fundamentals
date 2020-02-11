# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

def PrintStars(n):
    if n==0:
        return 1
    result = PrintStars(n-1) * n
    print('*' * result)
    return result

PrintStars(4)
