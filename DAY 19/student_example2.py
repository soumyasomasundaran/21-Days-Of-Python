from datetime import date


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: {}\nAge: {} ".format(self.name, self.age))

    @classmethod
    def find_age(cls, name, year_of_birth):
        return cls(name, (date.today().year - year_of_birth))  # Student('Meena',22)


s1 = Student('Tom', 19)
s2 = Student.find_age('Meena', 1999)  # s2 = Student('Meena',22)
s3 = Student.find_age('Alex', 1967)
s1.display()
s2.display()
s3.display()
