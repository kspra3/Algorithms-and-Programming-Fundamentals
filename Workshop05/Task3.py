# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

#In order to improve the readability of the output, we take as input a list containing distance/cost pairs and prints the one pair on each line.
def printList(array):
    for row in array:
        stringFormatted = str(row[0]) + " kms, " + "$" + str(row[1])
        print(stringFormatted)

def selectionSortPrice(array):
    vendor = len(array)
    for position in range(vendor - 1):
        minRow = position
        for temp in range(position + 1, vendor):
            if array[temp][1] < array[minRow][1]:
                minRow = temp
        array[position], array[minRow] = array[minRow], array[position]
    return array

fileName = input("Enter name of file: ")
data = open(fileName)
table = []
row = 0
for line in data:
    table.append(line.split(','))
    table[row][0] = int(table[row][0])
    table[row][1] = float(table[row][1])
    row += 1
data.close()
table = selectionSortPrice(table)
printList(table)