# Debugging Assistance 
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide_numbers(10, 0)
    print(result)
except ValueError as e:
    print(f"Error: {e}")

# Example of successful division
try:
    result = divide_numbers(10, 2)
    print(f"10 divided by 2 is: {result}")
except ValueError as e:
    print(f"Error: {e}")
