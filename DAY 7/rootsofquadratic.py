from math import sqrt


def discriminant(a, b, c):
    return (b * b) - (4 * a * c)


def quadratic(a, b, c):
    d = discriminant(a, b, c)
    if d > 0:
        root1 = ((-b) + (sqrt(d))) / (2 * a)
        root2 = ((-b) - (sqrt(d))) / (2 * a)
        print("Roots of the quadratic equation are", root1, "and", root2)
    elif d == 0:
        root = (-b) / (2 * a)
        print("Quadratic Equation has one root", root)
    else:
        print("Quadratic Equation has no roots")


print("Enter the coefficients of the quadratic equation aX^2+bx+C")
a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
quadratic(a, b, c)
