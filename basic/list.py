L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# l 为一个 list， g 为 generator 即 生成器
l = [x * x for x in range(3)]
g = (x * x for x in range(3))
print(l) # [0, 1, 4]
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 4


test = [1, 1]
print(len(test) - 1) # 1
print(range(len(test) - 1)) # range(0, 1) 左闭右开
print(list(range(len(test) - 1))) # [0]
for i in range(len(test) - 1):
    print(i) # 0
    print(test[i], test[i+1]) # 1 1

# 可使用 for 循环 ，一类是集合数据类型，如list、tuple、dict、set、str等；一类是generator，包括生成器和带yield的generator function
# isinstance 判断对象类型