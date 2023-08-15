import pyinputplus as pyip


def addsUpToTen(numbers):
    numberList = list(numbers)
    for i, digits in enumerate(numberList):
        numberList[i] = int(digits)
        if sum(numberList) != 10:
            raise Exception('The digits must add up to 10, not %s.' % (sum(numberList)))
        return int(numbers)

print("Enter a number that is adds up to 10")

responses = pyip.inputCustom(addsUpToTen)
