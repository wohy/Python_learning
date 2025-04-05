import functools
# 创建偏函数
int2 = functools.partial(int, base=2)
# 等同于
# def in2(x):
#     int(x, base=2)

# 偏函数固定住 base 为 2
print(int2('1000000')) # 64

# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
