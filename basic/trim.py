def trim(s):
    # return s.strip()
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    end = len(s) - 1
    while end >= 0 and s[end] == ' ':
        end -= 1
    return s[start:end + 1]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')