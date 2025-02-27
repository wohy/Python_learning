from functools import reduce

def is_number(value):
    # """判断变量是否为 int/float/complex 且 非bool 类型, bool 是 int 的子类"""
    return isinstance(value, (int, float, complex)) and not isinstance(value, bool)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int1(s: str):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
theInt1 = str2int1('1234')
print(theInt1, f'是否数字{is_number(theInt1)}') # 1234 是否数字True


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s: str):
    return DIGITS[s]

def str2int2(s: str):
    # lambda x, y: x * 10 + y 等同于 js 中的箭头函数 (x, y) => x * 10 + y，写法不同而已
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
theInt2 = str2int2('12345')
print(theInt2, f'是否数字{is_number(theInt2)}') # 12345 是否数字True

print(True == 1) # True