from collections import Iterable
# Dictionary
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(d.get(key))
print(isinstance(d, Iterable))

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# Practice
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    minValue = maxValue = L[0]
    for value in L:
        if value < minValue:
            minValue = value
        if value > maxValue:
            maxValue = value
    return (minValue, maxValue)


