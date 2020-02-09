# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

fileName = input ("Please enter the filename : ")
list = []
data = open(fileName)

for line in data :
    temp = line.strip("\n") # Remove the new line character at the end.
    temp = temp.split("\t") # Split the line after the tab.
    temp[1] = temp[1].split(',') # Split what’s after the tab.
    list .append(temp)

data.close()
pairedList =[]
for row in list:
    for element in range (1 , len(row)):
        pair = [row[0],row[element]]
        pairedList.append(pair)

print(pairedList)