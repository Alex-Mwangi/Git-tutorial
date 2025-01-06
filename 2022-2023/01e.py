
# swapping 2 numbers

j = 10
i = 20

# first approach
# i, j = j, i

# print('j=',j)
# print('i=',i)


# second appoach, using the third variable
# temp = i
# i = j
# j = temp

# print('j=',j)
# print('i=',i)

# using the 3 approach, without using the 3 variables

i = i + j
j = i - j
i = i - j

print('j=',j)
print('i=',i)
