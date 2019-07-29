# Calculates the real roots of a quadratic equation
#    The equation is in the from a*x**2+b*x+c
#    The solution is x = (-b +- sqrt(discriminant))
#    The discriminant is b**2 + 4*a*c

from math import sqrt

a = float(input("Give the value of a: "))
b = float(input("Give the value of b: "))
c = float(input("Give the value of c: "))

discr = b**2 - 4*a*c

if a == 0:
    print("This is a linear equation")
    x = -c/b
    print("x:", x)
elif discr < 0:
    print("The function does not have any real roots")
elif discr > 0:
    print("The function has two roots")
    x1 = (-b + sqrt(discr)) / (2*a)
    x2 = (-b -sqrt(discr)) / (2*a)
    print("x1: ", x1, "\tx2: ", x2)
else:
    print("The function has exactly one root")
    x = -b
    print("x:", x)
