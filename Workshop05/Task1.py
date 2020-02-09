# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

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
print(table)
