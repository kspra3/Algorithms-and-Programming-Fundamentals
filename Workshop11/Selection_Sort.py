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
    return l

test_list = [1,12,3,6,9,10,2,4]
sorted_list = SelectionSort(test_list)
print(sorted_list)
