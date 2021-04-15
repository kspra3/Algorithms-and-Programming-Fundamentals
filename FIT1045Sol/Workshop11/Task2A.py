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

'generate random integers for x and n'
x = random.randrange(1,100)
n = random.randrange(1,100)

'start timing power1'
start = timeit.default_timer()
power1(x,n)
'finish timing'
print("Time taken by power1 was: " + str(timeit.default_timer()-start) + " seconds.")


'start timing power2'
start = timeit.default_timer()
power2(x,n)

'finish timing power2'
print("Time taken by power2 was: " + str(timeit.default_timer()-start) + " seconds.")
