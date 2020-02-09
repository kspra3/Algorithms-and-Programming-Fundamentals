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


def BinarySearch2(L,query):
    if len(L)<= 0:
        return -1
    else:
        middleIndex = (len(L))// 2
        if L[middleIndex][1] == query:
            return middleIndex
        elif L[middleIndex][1] > query:
            return BinarySearch2(L[:middleIndex],query)
        elif L[middleIndex][1] < query:
            return BinarySearch2(L[middleIndex+1:],query) + len(L[:middleIndex+1])
            
    

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
index = BinarySearch2(sortedData,suburb.title())
if index !=-1:
    print('Post code is %d' % sortedData[index][0])
else:
    print('Not Found')
