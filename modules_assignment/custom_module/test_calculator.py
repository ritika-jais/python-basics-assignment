import calculator  # Import the custom module

try:
    num1 = float(input("Enter first number: "))  # Convert user input to float
    num2 = float(input("Enter second number: "))

    result = calculator.divide(num1, num2)  # Call divide function from calculator module

    print("Result:", result)  # Display output

except ValueError:
    print("Error: Please enter valid numeric values.")  # Handle non-numeric input
