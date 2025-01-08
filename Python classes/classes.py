
# classes in python

class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def greet(self):
        print(f"Hello {self.name}, you're {self.age} years old and {self.height} feet high.")

person1 = Person('Alex', 20, 5)
person1.greet()

print(person1.name)