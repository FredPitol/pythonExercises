## User grade input
grade1 = float(input('Enter the grade for the first quarter: '))
grade2 = float(input('Enter the grade for the second quarter: '))
courseAverage = (grade1 + grade2) / 2

## Processing data
if courseAverage < 3:
    print(f'Your average is{courseAverage: .2f}\nSorry course failure')
elif courseAverage < 7:
    finalExam = float(input('Enter the final exam grade'))
    if finalExam < 5:
        print('Course failure')
    elif (finalExam >= 5) and (finalExam <= 10):
        print('You pass the course')
    else:
        print('Invalid grade')
elif courseAverage <= 10:
    print(f'Your average is{courseAverage: .2f}\nCongratulations, you pass the course!')
else:
    print('Invalid grade')
