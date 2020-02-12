import random
import timeit

def power1(x, n):
    'computes x to the power of n'

    value = 1
    for k in range(n):
        value *= x
    return value

def power2(x,n):
    'computes x to the power of n'
    value = 1

    if n > 0:
        value = power2(x, n // 2)
    if n % 2 == 0:
        value = value * value
    else:
        value = value * value * x

    return value

data1 = []
data2 = []

for i in range (100):
    'generate random integers for x and n'
    x = random.randrange(1,100)
    n = random.randrange(1,100)

    'start timing power1'
    start = timeit.default_timer()
    power1(x,n)
    duration1 = timeit.default_timer()-start
    data1.append([x,n,duration1])
    
    'start timing power2'
    start = timeit.default_timer()
    power2(x,n)
    duration2 = timeit.default_timer()-start
    data2.append([x,n,duration2])

bestIndex1 = 0
worstIndex1 = 0
bestIndex2 = 0
worstIndex2= 0

for i in range(1,100):
    if data1[bestIndex1][2] > data1[i][2]:
        bestIndex1 = i

    if data1[worstIndex1][2] < data1[i][2]:
        worstIndex1 = i

    if data2[bestIndex2][2] > data2[i][2]:
        bestIndex2 = i

    if data2[worstIndex2][2] < data2[i][2]:
        worstIndex2 = i

print('Best for power1 was x=%d, n=%d and time %.10f seconds.' % (data1[bestIndex1][0],data1[bestIndex1][1],data1[bestIndex1][2]))
print('Worst for power1 was x=%d, n=%d and time %.10f seconds.' % (data1[worstIndex1][0],data1[worstIndex1][1],data1[worstIndex1][2]))

print('Best for power2 was x=%d, n=%d and time %.10f seconds.' % (data2[bestIndex2][0],data2[bestIndex2][1],data2[bestIndex2][2]))
print('Worst for power2 was x=%d, n=%d and time %.10f seconds.' % (data2[worstIndex2][0],data2[worstIndex2][1],data2[worstIndex2][2]))
