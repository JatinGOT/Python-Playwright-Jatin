class BasicCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error! Division by zero is not allowed."
        return self.num1 / self.num2

    def modulus(self):
        if self.num2 == 0:
            return "Error! Modulus by zero is not allowed."
        return self.num1 % self.num2

    def power(self):
        return self.num1 ** self.num2


# Main Program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

calculator = BasicCalculator(num1, num2)

print("\nChoose Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")

choice = int(input("Enter your choice (1-6): "))

if choice == 1:
    print("Result:", calculator.add())
elif choice == 2:
    print("Result:", calculator.subtract())
elif choice == 3:
    print("Result:", calculator.multiply())
elif choice == 4:
    print("Result:", calculator.divide())
elif choice == 5:
    print("Result:", calculator.modulus())
elif choice == 6:
    print("Result:", calculator.power())
else:
    print("Invalid choice!")