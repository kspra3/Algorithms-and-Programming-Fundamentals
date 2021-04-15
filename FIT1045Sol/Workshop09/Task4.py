# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

def printList(T):
    print('Index\tCode\tTown')
    print('----------------------------')
    for i in range (len(T)):
        print(i,'\t',T[i][0],'\t',T[i][1])

def partitionTowns(T,p):
    start = 0
    boundary = start
    T = swapValue(T,boundary,p)
    pivot = T[0][1]

    for i in range(1,len(T)):
        if T[i][1] < pivot:
            boundary += 1
            T = swapValue(T,boundary,i)

    T = swapValue(T,start,boundary)

    subList1 = T[0:2]
    subList2 = T[boundary:len(T)]
    printList(subList1)
    print('\n')
    printList(subList2)
    return boundary
    


def swapValue(T,i,j):
    tempLocation = T[i][1]
    tempPostcode = T[i][0]
    T[i][1]= T[j][1]
    T[i][0]= T[j][0]
    T[j][1] = tempLocation
    T[j][0] = tempPostcode
    return T



filename = input('Enter name of postcode file: ')
infile = open(filename,'r')
contents = infile.readlines()
infile.close()

data = []
for i in range (len(contents)):
    infoStr = contents[i]
    infoList = infoStr.split('\t')
    postcode = int(infoList[0])
    locationList = infoList[1].split(',')
    for j in range(len(locationList)):
        locationList[j] = locationList[j].rstrip('\n')
        data.append([postcode,locationList[j]])

printList(data)
print('\n')
position = int(input('Select an index of the list: '))
print('\n')
print('Undated Lists:')

partitionTowns(data,position)
