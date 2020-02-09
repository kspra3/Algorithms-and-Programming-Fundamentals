# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

#In order to improve the readability of the output, we take as input a list containing distance/cost pairs and prints the one pair on each line.
def printList(array):
    for row in array:
        stringFormatted = str(row[0]) + " kms, " + "$" + str(row[1])
        print(stringFormatted)

def selectionSort(array, field):
    vendor = len(array)
    for position in range(vendor - 1):
        minRow = position
        for temp in range(position + 1, vendor):
            if array[temp][field] < array[minRow][field]:
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
userChoice =""
while not userChoice == "Quit ":
    userChoice = input(" Enter choice ( Print / Sort1 ( dist ) / Sort2 ( price / Quit : ")
    if userChoice=="Sort1":
        printList(selectionSort(table ,0))
    elif userChoice=="Sort2":
        printList(selectionSort(table ,1))
    elif userChoice=="Print":
        printList(table)
    elif userChoice=="Quit":
        print("Quitting ...")
    else :
        print (" Invalid input ")
