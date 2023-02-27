# Printing only the even numbers between 1 and 10 

print("The even numbers between 1 and 10 is: \n")
for contador in range (0, 11, 1):
    if (contador & 1 == 0 ):
        print(f"Number even: {contador}")