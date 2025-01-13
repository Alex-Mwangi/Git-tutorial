
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
    

p1 = Person('Alex', 30)
print(p1)

class Student(Person):

    def __init__(self, name, age, regno):
        super().__init__(name, age)