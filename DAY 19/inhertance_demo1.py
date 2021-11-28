class Animal:
    def make_sound(self):
        print("Make Sound")

    def print_animal(self):
        print("I am an animal")


class Dog(Animal):
    def make_sound(self):
        print("Bark Bark")


class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")


# calling function from parent class
d1 = Animal()
d1.make_sound()

d2 = Dog()
d2.make_sound()
d2.print_animal()

c1 = Cat()
c1.make_sound()
c1.print_animal()