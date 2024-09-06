def division():
    try:
        num1 = int(input("Enter the first number (dividend): "))
        num2 = int(input("Enter the second number (divisor): "))
        
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    except ValueError:
        print("Error: Invalid input. Please enter valid integer numbers.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

division()
