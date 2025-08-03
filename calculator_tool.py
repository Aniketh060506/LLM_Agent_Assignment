# calculator_tool.py

def add(a, b):
    """Adds two numbers."""
    return float(a) + float(b)

def multiply(a, b):
    """Multiplies two numbers."""
    return float(a) * float(b)

def subtract(a, b):
    """Subtracts two numbers."""
    return float(a) - float(b)

def divide(a, b):
    """Divides two numbers, with a check for division by zero."""
    if float(b) == 0:
        return "Error: Division by zero is not allowed."
    return float(a) / float(b)
