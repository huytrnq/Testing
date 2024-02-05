

def add(x, y):
    """Add function

    Args:
        x (number): first number
        y (number): second number

    Returns:
        number: result of x + y
    """
    return x + y

def mutiply(x, y):
    """Multiply function

    Args:
        x (number): first number
        y (number): second number

    Returns:
        number: result of x * y
    """
    return x * y

def subtract(x, y):
    """Subtract function

    Args:
        x (number): first number
        y (number): second number

    Returns:
        number: result of x - y
    """
    return x - y

def divide(x, y):
    """Divide function

    Args:
        x (number): first number
        y (number): second number

    Returns:
        number: result of x / y
    """
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y