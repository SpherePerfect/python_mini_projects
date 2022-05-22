print("\033[1m" + "CALCULATOR")

operations_list = ["addition", "subtraction", "multiplication", "division"]

numberOneInput = input("Enter the first number:")

numberTwoInput = input("Enter the second number:")

operationInput = input("Enter the operation you want to perform:")

numberOne = float(numberOneInput)
numberTwo = float(numberTwoInput)
operation = str(operationInput)

if operation in operations_list:

    if operation == "multiplication":
        if numberOne == 45 and numberTwo == 3:
            print("Answer is: 555")
        else:
            print("The answer is:",numberOne * numberTwo)

    if operation == "addition":
        if numberOne == 56 and numberTwo == 9:
            print("Answer is: 77")
        else: print("Answer is:", numberOne + numberTwo)

    if operation == "division":
        if numberOne == 56 and numberTwo == 6:
            print("The answer is: 4")
        else:
            print("The answer is:",numberOne/numberTwo)

    if operation == "subtraction":
        if numberOne == 56 and numberTwo == 6:
            print("The answer is: 12")
        else:
            print("The answer is:",numberOne - numberTwo)
else:print("ERROR!")

