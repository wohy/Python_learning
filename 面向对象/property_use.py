class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @width.setter
    def width(self, val):
        self._width = val
    @height.setter
    def height(self, val):
        self._height = val
    @property
    def resolution(self):
        return self._height * self._width
    pass

# 测试:
s = Screen()
s.width = 1024
s.height = 768
# s.resolution = 12 # resolution 只读，设置值会报错：AttributeError: can't set attribute
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')