print("Calculating the hypotenuse of a right triangle with legs B and C\n")
B = float(input("Insert the value of the leg B:\n"))
C = float(input("Insert the value of the leg C:\n"))

# Data processing
B = B ** 2
C = C ** 2
H = (B + C) ** 0.5

# Result
print(f"The hypotenuse of the right triangle is{H: .2f}")
