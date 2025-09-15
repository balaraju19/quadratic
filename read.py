import math
with open('coefficients.txt', 'r') as file:
    a, b, c = map(float, file.readline().split())
d = b**2 - 4*a*c
if d >= 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are:", r1, "and", r2)
else:
    print("No real roots, discriminant is negative.")