#--------------------------------
# 1. Loop
#--------------------------------
# for...in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in list(range(101)):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

#--------------------------------
# 2. Break
#--------------------------------
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n += 1
print("end")

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)


#--------------------------------
# 3. Practice
#--------------------------------
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello, %s!" %(name))

