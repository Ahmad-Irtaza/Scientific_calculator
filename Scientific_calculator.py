import math

class SciCalculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y != 0:
            self.result = x / y
        else:
            print("Error: Division by zero")

    def power(self, x, y):
        self.result = x ** y

    def square_root(self, x):
        if x >= 0:
            self.result = math.sqrt(x)
        else:
            print("Error: Cannot calculate square root of a negative number")


calculator = SciCalculator()

while True:
    print("\nScientific Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Quit")

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5', '6']:
        try:
            if choice == '6':
                num1 = float(input("Enter a number: "))
                calculator.square_root(num1)
            else:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    calculator.add(num1, num2)
                elif choice == '2':
                    calculator.subtract(num1, num2)
                elif choice == '3':
                    calculator.multiply(num1, num2)
                elif choice == '4':
                    calculator.divide(num1, num2)
                elif choice == '5':
                    calculator.power(num1, num2)

            print("Result: ", calculator.result)
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
    else:
        print("Error: Invalid choice. Please enter a number between 1 and 7.")
