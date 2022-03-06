from cmath import *


solutions = set()

def cbrt(polynom):
    solution = set()
    root1 = polynom ** (1 / 3)
    root2 = (polynom ** (1 / 3)) * (-1 / 2 + (sqrt(3) * complex(0, 1)) / 2)
    root3 = (polynom ** (1 / 3)) * (-1 / 2 - (sqrt(3) * complex(0, 1)) / 2)
    solution.update({root1, root2, root3})
    return solution

print('ax^3+bx^2+cx+d=0')
a, b, c, d = map(complex, input().split())

p = (3 * a * c - b ** 2) / (3 * a ** 2)
q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d)/(27 * a ** 3)
alpha = cbrt(-q/2 + sqrt((q/2) ** 2 + (p/3) ** 3))
beta = cbrt(-q/2 - sqrt((q/2) ** 2 + (p/3) ** 3))
for i in alpha:
    for j in beta:
       if abs((i * j) + p/3) <= 0.00001:
           x = i + j - b/(3 * a)
           solutions.add(x)

print(solutions)
