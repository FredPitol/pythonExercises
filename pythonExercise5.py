# User input
B = int(input('Insert your birth date: '))

# Processing data
if (B >= 2012) and (B <= 2023):
    print("You're a alpha")

elif (B >= 2003) and (B <= 2011):
    print('You belong to generation z')

elif (B >= 1989) and (B <= 2002):
    print('You belong to generation y')

elif (B >= 1974) and (B <= 1988):
    print('You belong to generation x')

elif (B >= 1959) and (B <= 1973):
    print("You're a baby boomer")

elif (B >= 1901) and (B <= 1958):
    print("You're a boomer")

else:
    print("You're dead")

