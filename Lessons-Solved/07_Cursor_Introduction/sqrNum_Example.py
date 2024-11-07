# Code Refactoring
def square_numbers(numbers):
    """
    Square each number in the input list using list comprehension.
    
    Args:
    numbers (list): A list of numbers
    
    Returns:
    A new list containing the squared values of the input numbers
    """
    return [num ** 2 for num in numbers]

# Example usage
example_list = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(example_list)
print(f"Original numbers: {example_list}")
print(f"Squared numbers: {squared_numbers}")
