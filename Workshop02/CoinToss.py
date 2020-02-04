# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

# Find the probability of getting heads in n number of coin flips using random() function
import random
nvalue = int(input("Please input the number of coin flips: "))

# Use variables to track the number of heads and tails
heads = 0
tails = 0

# Randomly generating heads or tails.
for i in range(nvalue):
    flip = random.random()
    if flip > 0.5:
        heads += 1
    else:
        tails += 1

# Printing the output.
print("The number of heads: ", heads, "\nThe number of tails: ", tails)
print("The ratio of heads to total tries is: ", heads/nvalue)
