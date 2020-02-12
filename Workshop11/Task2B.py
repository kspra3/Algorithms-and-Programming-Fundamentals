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

countItr = 0
countRec = 0

for i in range (100):
    'generate random integers for x and n'
    x = random.randrange(1,100)
    n = random.randrange(1,100)

    'start timing power1'
    start = timeit.default_timer()
    power1(x,n)
    duration1 = timeit.default_timer()-start

    'start timing power2'
    start = timeit.default_timer()
    power2(x,n)
    duration2 = timeit.default_timer()-start

    if duration1 < duration2:
        countItr+= 1
    else:
        countRec+= 1

print('Power1 faster: %d' % countItr)
print('Power2 faster: %d' % countRec)
