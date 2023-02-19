# User input
# Product price
P = float(input('Please input the product price: '))
# Quantity
Q = float(input('Please enter the quantity of products purchased: '))
# Total
T = Q * P
if T > 1000:
    D = T * (1-0.03*1)
    print(f'The total is R$:{T: .2f} with a 3% discount, the price of the product is R$:{D: .2f}')
else:
    print(f'The total is R$:{T: .2f}')

