import math

def quadratic(a, b, c):
    # 计算判别式
    discriminant = b**2 - 4*a*c
    # 根据判别式判断是否有实数根
    if discriminant > 0:
        # 有两个实数根
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # 有一个实数根
        root = -b / (2*a)
        return root
    else:
        # 没有实数根，返回None
        return None

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')