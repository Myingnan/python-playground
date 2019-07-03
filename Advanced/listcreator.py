# print 1~10
print(list(range(1, 11)))
# print x2 in 1~10
print([x * x for x in range(1, 11)])
# print x2 in 1~10 if is even number
print([x * x for x in range(1, 11) if x % 2 == 0])

# Dictionary
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, "-", v)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
