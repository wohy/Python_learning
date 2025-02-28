L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]  # 返回姓名

# by_name 返回姓名，
# by_name 作为排序的关键字传递给 sorted 函数。sorted 函数会根据 by_name 的返回值对列表进行排序，从而实现按姓名排序的效果。
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]  # 返回分数

# by_score 返回分数，
# by_score 作为排序的关键字传递给 sorted 函数。sorted 函数会根据 by_score 的返回值对列表进行排序，从而实现按分数排序的效果。
L2 = sorted(L, key=by_score)
print(L2)