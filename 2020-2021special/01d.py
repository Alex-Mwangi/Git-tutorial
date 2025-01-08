def sumDigits(n):
    """
    Computes the sum of the digits in an integer.

    Args:
        n: The integer.

    Returns:
        The sum of the digits in the integer.
    """

    if n < 0:
        n = -n  # Handle negative numbers

    total = 0
    while n > 0:
        total += n % 10  # Add the last digit to the total
        n //= 10  # Remove the last digit from the number

    return total

print(sumDigits(n=278))