# check which among 2 numbers is max

def findMax(firstNumber, secondNumber):
    if firstNumber > secondNumber:
        print("first number is greater!")
        return firstNumber
    elif secondNumber > firstNumber:
        print("second number is greater!")
        return secondNumber
    else:
        print("both numbers are equal!")
        return firstNumber

print("Enter the firt number: ")
firstNumber = int(input())
print("Enter the second number: ")
secondNumber = int(input())
maxnumber = findMax(firstNumber, secondNumber)
print("Max number = {}".format(maxnumber))