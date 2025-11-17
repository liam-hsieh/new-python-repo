
"""Example module demonstrating package-based imports.

This module is part of the libs package and shows how to organize
reusable code in a proper Python package structure.
"""

def import_checking1(test_str: str) -> str:
    """Check if package import is working correctly.
    
    This function demonstrates that the libs package can be imported
    successfully and provides a simple way to test the import system.
    
    Args:
        test_str: A test string to echo back with confirmation message
        
    Returns:
        A formatted string confirming successful import with the input string
        
    Example:
        >>> import_checking1("Hello World")
        'Import import_checking1 successful, and here is your input: Hello World'
    """
    return f"Import import_checking1 successful, and here is your input: {test_str}"

def calculate_sum(numbers: list[float]) -> float:
    """Calculate the sum of a list of numbers.
    
    Args:
        numbers: List of numbers to sum
        
    Returns:
        The sum of all numbers in the list
        
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric values
        
    Example:
        >>> calculate_sum([1, 2, 3, 4, 5])
        15.0
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    try:
        return float(sum(numbers))
    except (TypeError, ValueError) as e:
        raise ValueError("All items in list must be numeric") from e

def format_message(message: str, prefix: str = "INFO") -> str:
    """Format a message with a prefix.
    
    Args:
        message: The message content to format
        prefix: Prefix to add (default: "INFO")
        
    Returns:
        Formatted message string
        
    Example:
        >>> format_message("Processing complete", "SUCCESS")
        'SUCCESS: Processing complete'
    """
    return f"{prefix}: {message}"