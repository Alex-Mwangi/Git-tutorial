
# number = 12

# counter = 0

# for i in range(1, number+1):
#     if number % i == 0:
#         counter += 1

# if counter == 2:
#     print('prime')

# else:
#     print('not prime')

number = 70


primes = []

for i in range(1, number+1):

    counter = 0
    for j in range(1, i+1):
        if i % j == 0:
            counter += 1

    if counter == 2:
        primes.append(i)

print(primes)