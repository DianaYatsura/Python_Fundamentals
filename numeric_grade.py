"""
Create a Python program that asks the user for a numeric grade (0-100) and then uses conditional
statements to determine and print the corresponding letter grade (A, B, C, D, or F) A={90-100}
B={80-90} C={70-80} D={60-70} E={50-60} F={0-50}. If the number is less than 0 please print
the message - "Wrong number"
"""
def gradeCalculator(grade):
    match int(grade):
        case A if int(grade) in range(90, 100):
            print('A')
        case B if int(grade) in range(80, 90):
            print('B')
        case C if int(grade) in range(70, 80):
            print('C')
        case D if int(grade) in range(60, 70):
            print('D')
        case E if int(grade) in range(50, 60):
            print('E')
        case F if int(grade) in range(0, 50):
            print('F')
        case _:
            print('Wrong number')

#enter a grade for checking
gradeCalculator(grade=)


