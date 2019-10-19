# simpleCalc.py
# A rudimentary calculator that asks for two numbers then performs math

#Ask for numbers
print('Enter the first number:')
firstNum = int(input())
print('Enter the second number:')
secondNum = int(input())
5

#Choose operation
print('Choose operation +. -, *, or /')
operationValue = input()

#Math stuff
if operationValue == '+':
    print('{} + {} = '.format(firstNum, secondNum))
    print(firstNum + secondNum)
   

elif operationValue == '-':
    print('{} - {} = '.format(firstNum, secondNum))
    print(firstNum - secondNum)

elif operationValue == '*':
    print('{} * {} = '.format(firstNum, secondNum))
    print(firstNum * secondNum)

elif operationValue == '/':
    if firstNum < secondNum:
        print('Please enter larger value first')
    else:
         print('{} / {} = '.format(firstNum, secondNum))
         print(firstNum / secondNum)

else:
    print('Not valid operator!')
