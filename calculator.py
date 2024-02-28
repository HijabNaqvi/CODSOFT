# Simple Python Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "\n Cannot divide by zero!"
    return x / y

def get_operation():
    print("\n Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    while True:
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice in ('1', '2', '3', '4', '5'):
            return choice
        else:
            print("\n Invalid input")

def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def main():
    while True:
        choice = get_operation()
        if choice == '5':
            break
        num1, num2 = get_numbers()
        if choice == '1':
            print("\n Result:", add(num1, num2))
        elif choice == '2':
            print("\n Result:", subtract(num1, num2))
        elif choice == '3':
            print("\n Result:", multiply(num1, num2))
        elif choice == '4':
            print("\n Result:", divide(num1, num2))

if __name__ == "__main__":
    main()