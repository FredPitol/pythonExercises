# Calculatinng the area of  a rectangle

# Receive the values of the sides and the height of the rectangle
S = float(input("Insert the value in centimeters of the side of the rectangle: \n"))
H = float(input("Insert the value of the height in centimeters of the rectangle: \n"))

# Area = sides * height
A = S * H

# Print the result 
print(f"The area of the rectangle is{A: .2f}cm²")