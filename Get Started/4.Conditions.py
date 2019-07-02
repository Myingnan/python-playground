#--------------------------------
# 1. If
#--------------------------------
age = 20
if age >= 6 and age < 18:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

#--------------------------------
# 2. Input
#--------------------------------
birth = int(input("Birth: "))
if birth > 2000:
    print("New Joiner")
else:
    print("Old staff")

#--------------------------------
# 3. Practice
#--------------------------------
height = 1.75
weight = 80.5
bmi = weight/(height ** 2)
if bmi < 18.5:
    print("Too thin")
elif bmi > 18.5 and bmi < 25:
    print("Normal")
elif bmi > 25 and bmi < 28:
    print("Too wweight")
elif bmi > 28 and bmi < 32:
    print("Fat")
else:
    print("OMG...")

