def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform: 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: The result of the operation, or an error message if invalid input.
    """
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"
