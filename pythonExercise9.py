# Calculate and display the area and length of a circle by its radius
# Insert the value of the radius
R = float(input("Insert the value of the radius of the circle in centimeters: \n"))

# Calculate the area of the circle 
# area = 3,14 * radius * radius
A = 3.14 * R * R

# Calculate the lenght of the circle
# lenght = 2 * 3,14 * radius
L = 2 * 3.14 * R

# Print the result 
print(f"The area of the circle is{A: .2f}cm²\nThe leght of the circle is{L: .2f}cm²")

