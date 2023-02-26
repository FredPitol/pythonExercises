# Software that calculates the total 
#   of salary minus taxes and fees 

# Software que calcula o salario total 
#   descontando impostos e taxas 



# Inputting the number of hours worked
HW = float(input("Enter the number of hours worked:\n"))

# Inputting the amount paid per hour worked 
HP = float(input("Enter the amount paid per hour worked:\n"))

# Processing data 
# Total salary
T = HW * HP

# 8% INSS 
I = T*8/100

# 11% tax
TAX=T*11/100 

# 5% syndicate
SYN=T*5/100

# Deducted salary
DeSa= T-(I+TAX+SYN)

# Printing results 
print(f"Total salary:{T: .2f}\nINSS tax:{I: .2f}\nSyndicate fee:{SYN: .2f}\nTaxes:{TAX: .2f}\nDeducted salary{DeSa: .2f}\n")