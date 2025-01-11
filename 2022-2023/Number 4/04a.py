

filename = input("Enter the file name: ")

try:
    with open(filename, 'r') as file:
        data = file.read()
        print(data)

        numbers = list(map(int, data.split()))

        num = len(numbers)

        total = sum(numbers)
        average = total / len(numbers)

        print(f'There are {num} numbers in the list')

        print(total)
        print(average)
except FileNotFoundError:
    print("File not found")
