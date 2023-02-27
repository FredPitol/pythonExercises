import math
# Calculate and display the amount of paint (in cans) 
# and the cost (in dollars) to paint a cylindrical tank
# of circular base
can = 5 #liters
# 1 liter paint 3m²
# 1 can = 50 dollars 

# Inputting proportions
He = float(input("Enter the height of the cylinder in meters:\n"))
Ra = float(input("Enter the radius of the cylinder in meters:\n"))


# Calculating total area of the cylinder
# Total area = 2 * pi * radius * (radius + height)
ToAr = 2 * math.pi * Ra * (Ra + He)

# Printing results 
print(f"Total cylinder area:{ToAr: .2f}m²")
# https://www.youtube.com/watch?v=QEXABuduxZQ
