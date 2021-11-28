class Person():
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def display(self):
        print(f"Name:{self.name}\nID:{self.id}")

e1 = Employee('Marshall','S123')
e1.display()