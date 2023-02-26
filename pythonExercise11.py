import math

# Calculate the volume in liters of a sphere
# Insert the radius of the sphere
R = float(input("Insert the radius of the sphere in centimeters:\n"))

# Calculating the volume 
V = 4 / 3 * math.pi * R ** 3

# Round the number to the nearest tenth
V = round(V, 1)

# Printing the result
print(f"The volume of the sphere is: {V: .1f}cm³")