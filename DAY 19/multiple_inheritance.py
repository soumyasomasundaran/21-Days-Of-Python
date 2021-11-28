class Person():
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self,name,id):
        super().__init__(name)
        self.id = id

    def display(self):
        print("Name:{}\nID:{}".format(self.name,self.id))


t1 = Employee('Soumya','S123')
t1.display()


