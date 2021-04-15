# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

# Making a table of zeros.
# The number of row is obtained from the user.
Rows = int(input("Enter the number of rows for the table: "))
table = Rows * [0]

# We traverse through the rows.
rowNumber = 0
while rowNumber < Rows:
    # Split the user input and store it in a temporary list.
    temp = input("Enter some numbers: ").split()
    # Make the current row a zero list of same size as number of input
    table[rowNumber] = len(temp) * [0]
    for colNumber in range(len(temp)):
        # Cast each "cell" as float and insert to the table.
        table[rowNumber][colNumber] = float(temp[colNumber])
    rowNumber += 1
print(table)
