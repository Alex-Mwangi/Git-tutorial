
import random

menuitems = ['orange', 'banana', 'mango', 'apple', 'lemon']

orders = []

for item in range(1, 5):
    order = random.choice(menuitems)
    orders.append(order)

print(orders)