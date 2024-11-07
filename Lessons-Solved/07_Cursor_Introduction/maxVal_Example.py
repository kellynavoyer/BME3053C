#Natural Language Code Generation
def find_maximum(numbers):
    """
    Find the maximum value in a list of numbers using Python's built-in max() function.
    
    Args:
    numbers (list): A list of numbers
    
    Returns:
    The maximum value in the list, or None if the list is empty
    """
    if not numbers:
        return None  # Return None for an empty list
    
    return max(numbers)

# Example usage of the function
example_list = [10, 5, 8, 15, 3, 20, 12]
max_number = find_maximum(example_list)
print(f"The maximum value in the list is: {max_number}")

# Edge case: empty list
empty_list = []
max_number_empty = find_maximum(empty_list)
print(f"The maximum value in the empty list is: {max_number_empty}")

