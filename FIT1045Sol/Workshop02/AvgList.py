# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

# Calculate the average of a list (numbers received one at a time).
# We get the number of items from the user.
total = 0
counter = 0
numOfItems = int(input("Please input number of items: "))

# For every instance of the number of items, we obtain an integer.
while counter < numOfItems:
    intList = int(input("Please give me an integer: "))
    # Obtaining the sum of list.
    total = total + intList
    counter = counter + 1
#Obtaining the average of numbers in the list.
average = total / numOfItems

print(average)
