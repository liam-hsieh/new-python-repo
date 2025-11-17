
"""Example module demonstrating direct imports.

This module shows how to organize utility functions that are imported
directly from the same directory, without package structure.
"""

from datetime import datetime
from typing import Dict, Any

def import_checking2(test_str: str) -> str:
    """Check if direct import is working correctly.
    
    This function demonstrates that modules can be imported directly
    from the same directory without package structure.
    
    Args:
        test_str: A test string to echo back with confirmation message
        
    Returns:
        A formatted string confirming successful import with the input string
        
    Example:
        >>> import_checking2("Hello World")
        'Import import_checking2 successful, and here is your input: Hello World'
    """
    return f"Import import_checking2 successful, and here is your input: {test_str}"

def process_text(text: str) -> Dict[str, Any]:
    """Process text and return analysis information.
    
    Args:
        text: The text string to analyze
        
    Returns:
        Dictionary containing text analysis results including:
        - word_count: Number of words
        - char_count: Number of characters
        - processed_at: Timestamp of processing
        
    Example:
        >>> result = process_text("Hello world")
        >>> result['word_count']
        2
    """
    words = text.split()
    
    return {
        "word_count": len(words),
        "char_count": len(text),
        "processed_at": datetime.now().isoformat(),
        "original_text": text
    }

def validate_input(value: str, min_length: int = 1) -> bool:
    """Validate input string meets minimum requirements.
    
    Args:
        value: String to validate
        min_length: Minimum required length (default: 1)
        
    Returns:
        True if validation passes, False otherwise
        
    Example:
        >>> validate_input("test", 3)
        True
        >>> validate_input("hi", 3)
        False
    """
    return isinstance(value, str) and len(value.strip()) >= min_length