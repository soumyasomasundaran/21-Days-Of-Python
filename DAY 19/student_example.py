class Student:
    grace_mark = 10
    def __init__(self, name, id, physics, chemistry, maths):
        self.name = name
        self.id = id
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def find_total(self):
        self.total = self.physics + self.chemistry + self.maths+ Student.grace_mark
        print("Total mark is {}".format(self.total))

    @classmethod
    def change_gracemark(cls, grace_mark):
        cls.grace_mark = cls.grace_mark + grace_mark



s1 = Student('Meena', 'S123', 90, 79, 100)
s2 = Student('Alex', 'S234', 92, 80, 78)
Student.change_gracemark(20)
s1.find_total()
s2.find_total()


