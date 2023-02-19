# Password authenticator
# check if a number is odd or even and a multiple of 17
S = int(input('Insert your password: '))

if (S & 1) and (S & 17 == 0):
    print('Strong password')
else:
    print('Weak password')
