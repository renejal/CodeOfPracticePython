def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """subtrac fuction"""
    return x - y

def multiply(x, y):
    """Multipli function"""
    return x * y

def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError("Can not divide by zero!!")
    return (x / y)

