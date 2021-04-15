def SelectionSort_Location(T):
    for i in range (len(T)-1):
        minIndex = i
        minLocation= T[minIndex][1]
        postcode = T[minIndex][0]
        
        for j in range(i+1, len(T)):
            if minLocation > T[j][1]:
                minLocation = T[j][1]
                postcode = T[j][0]
                minIndex = j

        tempLocation = T[i][1]
        tempPostcode = T[i][0]
        T[i][1]= minLocation
        T[i][0]= postcode
        T[minIndex][1] = tempLocation
        T[minIndex][0] = tempPostcode
    return T

def BinarySearch1(L,query):
    minIndex = 0
    maxIndex = len(L)-1
    
    while minIndex <= maxIndex:
        middleIndex = (minIndex+maxIndex) // 2    
        if L[middleIndex][1] == query:
            return middleIndex
        elif L[middleIndex][1] > query:
            maxIndex = middleIndex - 1
        elif L[middleIndex][1] < query:
            minIndex = middleIndex + 1

    return -1

filename = input('Enter name of postcode file: ')
infile = open(filename,'r')
contents = infile.readlines()
infile.close()

suburb = input('Enter Suburb Name: ')

data = []
for i in range (len(contents)):
    infoStr = contents[i]
    infoList = infoStr.split('\t')
    postcode = int(infoList[0])
    locationList = infoList[1].split(',')
    for j in range(len(locationList)):
        locationList[j] = locationList[j].rstrip('\n')
        data.append([postcode,locationList[j]])

sortedData = SelectionSort_Location(data)
data_index = BinarySearch1(sortedData,suburb)
if data_index !=-1:
    print('Post code is %d' % sortedData[data_index][0])
else:
    print('Not Found')
