# K. Sharsindra Pratheen
# Advanced Computer Science
# Monash University

import math
# Input a decimal number as degrees.
# Convert it to Radians and display.
deg1 = float(input("Please enter the angle in degrees: "))
rad1 = deg1 * (math.pi/180)
print("Your angle in Radians: ", rad1)

# Print out cosine of this angle.
cos1 = math.cos(rad1)
print("Cosine of the angle: ", cos1)
