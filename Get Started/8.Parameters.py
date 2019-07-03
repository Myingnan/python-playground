#--------------------------------
# 1. Position
#--------------------------------
# def power(x):
#     return x * x

# print(power(5))
# print(power(15))

def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5, 2))
print(power(2, 10))
print(power(5))

def enroll(name, gender, age = 6, city = "Beijing"):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll("Sarah", "F")
enroll("Adam", "M", age = 18, city = "Dalian")

# Changable parameters
# result = a2 + b2 + ... + n2
# * => Tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n ** 2
    return sum

print(calc(1, 2))
nums = [1, 2, 3]
print(calc(*nums))

# Keywords parameter
# ** => Dictionary
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person("Michael", 30)
person("Bob", 35, city="Beijing", hobby="Football")

#--------------------------------
# 2. Practice
#--------------------------------
def product(*numbers):
    sum = 1
    for number in numbers:
        sum = sum * number
    return sum

