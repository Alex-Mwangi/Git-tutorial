first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

total = first_num + second_num

print(total)
    
option = input('Do you wish to continue. Enter yes or no: ')

option = option.lower()


while True:

    if option == 'yes':
        first_num = int(input("Enter first number: "))
        second_num = int(input("Enter second number: "))

        total = (first_num + second_num)

        print(total)

    elif option == 'no':
        break

    else:
        print('Invalid option')
        break




