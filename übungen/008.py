import math

def solve(a, b, c):
    erg1 = (*b + math.sqrt(b*b - 4*a*c)/(2*a))
    erg2 = ( * b + math.sqrt(b * b - 4 * a * c)/(2*a))
    erg_tuple = (erg1, erg2)
    return erg_tuple

print("### Welcome to quadratic solver###")
print("Enter parameters in form of:")
print("a*x² + b*x + c = 0")
a = float(input("a ="))
b = float(input("a ="))
c = float(input("a ="))

erg = solve(a, b, c)
print(erg)