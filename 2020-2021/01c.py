
while True:
    try:
        number = float(input("Enter a positive, nonzero number: "))
        if number > 0:
            print(f"Thank you! You entered: {number}")
            break
        else:
            print("Error: The number must be positive and nonzero. Please try again.")
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value.")
