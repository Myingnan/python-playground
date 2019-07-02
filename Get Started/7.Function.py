import math
#--------------------------------
# 1. Function
#--------------------------------
# Function defination
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad type!!!")
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-11))

# Null Function
def nop():
    pass

# Return multiple values
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#--------------------------------
# 2. Practice
#--------------------------------
# ax2 + bx + c = 0
def quadratic(a, b, c):
    if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))) or (not isinstance(c, (int, float))):
        raise TypeError("Bad Type!")
    val1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    val2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return val1, val2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
