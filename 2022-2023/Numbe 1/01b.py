
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# a program that contains only even numers in list a

even_numbers = [even for even in a if even % 2 == 0]

print(even_numbers)