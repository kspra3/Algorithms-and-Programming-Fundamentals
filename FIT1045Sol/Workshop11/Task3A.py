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
    print(T)
    

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
    print(l)

data1 = [5,2,7,12,9,1,15,3]
Quicksort(data1)
data2 = [5,2,7,12,9,1,15,3]
SelectionSort(data2)
