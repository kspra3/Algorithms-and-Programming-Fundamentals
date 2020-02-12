import random
import timeit

def partition(T,first,last):
    pivot = T[first]
    boundary = first
    for i in range(first+1,last+1):
        if T[i] < pivot:
            boundary += 1
            T = swapValue(T,boundary,i)

    T = swapValue(T,first,boundary)
    return boundary

   
def swapValue(T,i,j):
    temp = T[i]
    T[i]= T[j]
    T[j] = temp
    return T

def Quicksort(T):
    start = 0
    end = len(T) - 1
    Quicksort_aux(T,start,end)
    

def Quicksort_aux(T,first,last):
    if first < last:
        splitPoint= partition(T,first,last)
        Quicksort_aux(T,first,splitPoint-1)
        Quicksort_aux(T,splitPoint+1,last)

def SelectionSort(l):
    for i in range (len(l)-1):
        minValue = l[i]
        minIndex = i
        for j in range(i+1, len(l)):
            if minValue > l[j]:
                minValue = l[j]
                minIndex = j

        tempValue = l[i]
        l[i]= minValue
        l[minIndex] = tempValue
    

def timeSort():
    big_list = []    
    for i in range(100):
        L = []
        for j in range(10):
            num = random.randrange(1,100)
            L.append(num)

        start = timeit.default_timer()
        Quicksort(L)
        duration = timeit.default_timer() - start
        big_list.append([L,duration])

    bestIndex = 0
    worstIndex = 0
    for i in range(1,len(big_list)):
        if big_list[bestIndex][1] > big_list[i][1]:
            bestIndex = i

        if big_list[worstIndex][1] < big_list[i][1]:
            worstIndex = i

    print('Shortest time taken was %.10f seconds.' % big_list[bestIndex][1] )
    print(big_list[bestIndex][0])

    print('Longest time taken was %.10f seconds.' % big_list[worstIndex][1] )
    print(big_list[worstIndex][0])
    
timeSort()
