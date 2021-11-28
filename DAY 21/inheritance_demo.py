class Animal:
    def print_animal(self):
        print("I am an animal")

    def make_sound(self):
        print("makes sound")

class Dog(Animal):

    def make_sound(self):
        print("Bark Bark")

class Cat(Animal):
    pass


d1 = Dog()
d1.make_sound()

a1 = Animal()
a1.make_sound()

c1 = Cat()
c1.make_sound()
