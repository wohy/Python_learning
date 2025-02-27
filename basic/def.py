# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
def mul(args, *args1):
    result = args
    for num in args1:
        result *= num
    return result

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')



# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
args = (1, 2, 3, 4, 5)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw) # a = 1 b = 2 c = 3 args = (4, 5) kw = {'d': 99, 'x': '#'}
