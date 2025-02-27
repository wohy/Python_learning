def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(source, '-->', target)
    else:
        # 把n-1个盘子从源移动到辅助，借助目标
        hanoi(n-1, source, target, auxiliary)
        # 把最后一个盘子从源移动到目标
        hanoi(1, source, auxiliary, target)
        # 把n-1个盘子从辅助移动到目标，借助源
        hanoi(n-1, auxiliary, source, target)
# Example usage
hanoi(3, 'A', 'B', 'C')