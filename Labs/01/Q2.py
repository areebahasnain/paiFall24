num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number...again: "))

operation = input("Enter an operation (+, -, *, /): ")

if(operation == '-'): print("Result:", num1 - num2)
elif operation == '*': print("Result:", num1 * num2)
elif operation == '/': 
    if(num2 != 0): print("Result:", num1/num2)
    else: print("Division by zero is undefined")
elif operation == '+': print("Result:", num1 - (-num2))
else: print("Invalid operation!")

    

