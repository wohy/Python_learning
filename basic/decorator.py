# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
# 假设我们要增强函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改函数本身的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

# decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log_decorator(func):
    def wrapper(*args, **kw):
        print('call %s' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log_decorator
def now():
    print('2025-04-05')

now()
# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)


# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        res = fn(*args, **kw)
        end_time = time.time()
        duration_ms = (end_time - start_time) * 1000
        print(f"{fn.__name__} executed in {duration_ms:.2f} ms")
        return res
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 设计一个既支持传参调用 @log('execute') 又支持直接调用 @log 的装饰器
def log(*args_or_func):
    # 判断是否带参数调用装饰器
    if len(args_or_func) == 1 and callable(args_or_func[0]):
        # 不带参数的情况：直接装饰函数
        fn = args_or_func[0]
        decorator = create_decorator()
        return decorator(fn)
    else:
        # 带参数的情况：返回装饰器工厂
        return create_decorator(*args_or_func)

def create_decorator(*args):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args_wrap, **kwargs_wrap):
            if args:
                print(f"{fn.__name__} executed")  # 带参数时输出
            else:
                print(f"call {fn.__name__}")       # 不带参数时输出
            return fn(*args_wrap, **kwargs_wrap)
        return wrapper
    return decorator

@log
def f1():
    pass
@log('execute')
def f2():
    pass

f1()
f2()