grade1 = float(input('Enter the grade for the first quarter: '))
grade2 = float(input('Enter the grade for the second quarter: '))
courseAverage = (grade1 + grade2) / 2

if courseAverage < 5:
    print(f'Your average is{courseAverage: .2f} this is less than the average 5, sorry but you repeat the course')
else:
    print(f'Your average is{courseAverage: .2f} this is more than the average 5, congratulations, you pass the course!')
