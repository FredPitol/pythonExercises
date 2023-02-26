# Calculate and display the bmi of a person 

# Inserting the weight in kilograms
W = float(input("Insert the weight in kilograms: \n"))

# Inserting the height in meters
H = float(input("Insert the height in meters: \n")) 

# Processing the data bmi = weight / (height * height)
BMI = W / (H*H)

# Print the result
print(f"Your bmi is:{BMI: .2f}")