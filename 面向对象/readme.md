# 类和示例
定义一个 Student 类
```py
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
```
- 特殊方法
特殊方法前后分别有两个下划线
`__init__` 初始化示例方法；
`__slots__` 指定示例上的属性

- 私有变量
以 `__` 开头，如定义 `__name`
不能直接访问 `__name` 是因为Python解释器对外把 `__name` 变量改成了 `_Student__name`，所以，仍然可以通过 `_Student__name` 来访问 `__name` 变量


# isinstance
判断 某个对象是否是 某个类的实例，是的话返回 True ，子类的实例，父类也会返回 True

# 继承 和 多态
继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

# 获取对象信息
### 1. 使用type()
- 基本类型都可以用type()判断
``` shell
    >>> type(123)
    <class 'int'>
    >>> type('str')
    <class 'str'>
    >>> type(None)
    <type(None) 'NoneType'>
```
- 如果一个变量指向函数或者类，也可以用type()判断：
```shell
    >>> type(abs)
    <class 'builtin_function_or_method'>
    >>> type(a)
    <class '__main__.Animal'>
```
- 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的 type 类型是否相同：
```shell
    >>> type(123)==type(456)
    True
    >>> type(123)==int
    True
    >>> type('abc')==type('123')
    True
    >>> type('abc')==str
    True
    >>> type('abc')==type(123)
    False
```
- 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
```shell
    >>> import types
    >>> def fn():
    ...     pass
    ...
    >>> type(fn)==types.FunctionType
    True
    >>> type(abs)==types.BuiltinFunctionType
    True
    >>> type(lambda x: x)==types.LambdaType
    True
    >>> type((x for x in range(10)))==types.GeneratorType
True
```

### 2. 使用isinstance()
对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
除了判断自己创建实例的继承关系
- 还能用type()判断的基本类型也可以用isinstance()判断：
```shell
    >>> isinstance('a', str)
    True
    >>> isinstance(123, int)
    True
    >>> isinstance(b'a', bytes)
    True
```
- 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
```shell
    >>> isinstance([1, 2, 3], (list, tuple))
    True
    >>> isinstance((1, 2, 3), (list, tuple))
    True
```

### 3. 使用dir()
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
```shell
>>> dir('ABC')
['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
```
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。

- 对象上的 getattr()、setattr() 以及 hasattr() 方法，在不确定对象属性时使用，可以直接使用 `.` 运算符，就直接使用 `.`
```shell
    >>> hasattr(obj, 'x') # 有属性'x'吗？
    True
    >>> obj.x
    9
    >>> hasattr(obj, 'y') # 有属性'y'吗？
    False
    >>> setattr(obj, 'y', 19) # 设置一个属性'y'
    >>> hasattr(obj, 'y') # 有属性'y'吗？
    True
    >>> getattr(obj, 'y') # 获取属性'y'
    19
    >>> obj.y # 获取属性'y'
    19
```

# 实例属性 和 类属性
- 实例绑定属性的方法是通过实例变量，或者通过self变量
```py
class Student(object):
    def __init__(self, name):
        self.name = name
    s = Student('Bob')
    s.score = 90
```
- 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
```py
    class Student(object):
    name = 'Student'
```
## 总结
实例属性属于各个实例所有，互不干扰；
类属性属于类所有，所有实例共享一个属性；

在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

#  __slots__
在 Python 的面向对象编程中，`__slots__` 是一个特殊的类属性，用于优化类的实例。它的核心作用如下：
---

### **1. 限制实例可添加的属性**
• **默认行为**：Python 类的实例会动态地将属性存储在 `__dict__` 字典中，允许运行时随意添加新属性。
• **使用 `__slots__`**：  
  定义 `__slots__` 后，实例只能拥有 `__slots__` 中指定的属性，**无法动态添加其他属性**，避免拼写错误或意外扩展。
  
  ```python
  class User:
      __slots__ = ["name", "age"]
  
  u = User()
  u.name = "Alice"  # 允许
  u.email = "alice@example.com"  # 报错: AttributeError
  ```

---

### **2. 优化内存占用**
• **默认问题**：每个实例的 `__dict__` 字典会占用额外内存，尤其是当创建大量实例时（例如百万级对象）。
• **`__slots__` 优化**：  
  使用 `__slots__` 后，实例通过 **固定大小的数组** 存储属性，不再维护 `__dict__`，可显著减少内存开销。  
  **示例内存对比**：  
  ```python
  class WithoutSlots: pass          # 默认类（有 __dict__）
  class WithSlots: __slots__ = ()   # 空 __slots__（禁用 __dict__）
  
  # 创建 1e6 个实例的内存占用
  # WithoutSlots: ~200 MB
  # WithSlots: ~80 MB
  ```

---

### **3. 提升属性访问速度**
• **底层机制**：属性访问从哈希表（字典）查找变为 **数组索引直接访问**，速度更快。
• **适用场景**：对性能敏感的代码（如高频调用的类方法）。

---

### **注意事项**
#### **继承行为**
• **父类有 `__slots__`，子类未定义**：  
  子类实例仍会有 `__dict__`，除非子类也定义 `__slots__`。
• **子类定义 `__slots__`**：  
  子类的 `__slots__` 会继承父类的 `__slots__`，并与自身定义的合并。  
  ```python
  class Parent:
      __slots__ = ["a"]
  
  class Child(Parent):
      __slots__ = ["b"]  # 实例可用的属性是 a + b
  ```

#### **灵活性限制**
• **无法动态添加属性**：必须预先在 `__slots__` 中声明所有可能的属性。
• **与 `__dict__` 冲突**：如果 `__slots__` 包含 `__dict__`，实例仍可动态添加属性，但会失去内存优化效果。
  ```python
  class Mixed:
      __slots__ = ["a", "__dict__"]  # 允许动态属性，但内存占用增加
  ```

#### **特殊方法依赖**
• **序列化/反序列化**：某些库（如 `pickle`）依赖 `__dict__`，使用 `__slots__` 时需额外处理。
• **弱引用（WeakRef）**：如需支持弱引用，需将 `__weakref__` 加入 `__slots__`。

---

### **何时使用 `__slots__`？**
• **场景**：
  1. 需要创建 **海量实例**（如数据处理、游戏实体）。
  2. 明确类的属性结构，**防止动态扩展**。
  3. 对 **内存和性能敏感** 的应用。
• **避免滥用**：普通场景无需使用，以免牺牲代码灵活性。

---

### **总结**
| **特性**               | **默认类（无 `__slots__`）**       | **使用 `__slots__` 的类**          |
|-------------------------|----------------------------------|-----------------------------------|
| 动态添加属性            | 支持                             | 仅允许 `__slots__` 中声明的属性    |
| 内存占用                | 较高（因 `__dict__`）            | 较低（数组存储属性）               |
| 属性访问速度            | 较慢（哈希表查找）               | 较快（直接索引）                   |
| 适用场景                | 通用开发                         | 性能优化、大规模实例、严格属性控制 |