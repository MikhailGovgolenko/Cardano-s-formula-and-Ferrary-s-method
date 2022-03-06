from cmath import *

solutions = set()
t = 0

def cbrt(polynom):
    solution = set()
    root1 = polynom ** (1 / 3)
    root2 = (polynom ** (1 / 3)) * (-1 / 2 + (sqrt(3) * complex(0, 1)) / 2)
    root3 = (polynom ** (1 / 3)) * (-1 / 2 - (sqrt(3) * complex(0, 1)) / 2)
    solution.update({root1, root2, root3})
    return solution

print('ax^4+bx^3+cx^2+dx+e=0')
a, b, c, d, e = map(complex, input().split())

p = (-3 * b ** 2 + 8 * a * c) / (8 * a ** 2)
q = (b ** 3 - 4 * a * b * c + 8 * a ** 2 * d) / (8 * a ** 3)
r = (-3 * b ** 4 + 16 * a * b ** 2 * c - 64 * a ** 2 * b * d + 256 * a ** 3 * e) / (256 * a ** 4)
p1 = (-p ** 2 - 12 * r) / 12
q1 = (-2 * p ** 3 + 72 * p * r - 27 * q ** 2) / 216
alpha = cbrt(-q1/2 + sqrt((q1/2) ** 2 + (p1/3) ** 3))
beta = cbrt(-q1/2 - sqrt((q1/2) ** 2 + (p1/3) ** 3))
for i in alpha:
    for j in beta:
       if abs((i * j) + p1/3) <= 0.00001:
           t = i + j - p/3
           break

x1 = (sqrt(2 * t) + sqrt(-(2 * t + 2 * p + sqrt(2 * t) * q/t)))/2 - b / (4 * a)
x2 = (-sqrt(2 * t) + sqrt(-(2 * t + 2 * p - sqrt(2 * t) * q/t)))/2 - b / (4 * a)
x3 = (sqrt(2 * t) - sqrt(-(2 * t + 2 * p + sqrt(2 * t) * q/t)))/2 - b / (4 * a)
x4 = (-sqrt(2 * t) - sqrt(-(2 * t + 2 * p - sqrt(2 * t) * q/t)))/2 - b / (4 * a)

solutions.update({x1, x2, x3, x4})
print(solutions)