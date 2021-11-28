class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def find_average(l):
        print("Your Average is ", sum(l)/len(l))

s1 = Student('Rami', 40)
s1.find_average([90, 72, 89, 56])

