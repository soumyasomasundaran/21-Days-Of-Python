class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def start(self):
        print("Vroom Vroom")

    def print_details(self):
        print("The Car name is {} and year is {}".format(self.name, self.year))


c1 = Car('Swift', '2007')
c2 = Car('Alto', '2018')
c2.print_details()
