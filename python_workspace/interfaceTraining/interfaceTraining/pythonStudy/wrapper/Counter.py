class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0  # 记录函数被调用的次数

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@Counter
def today(name='devin'):
    print('Hello, %s! Today is 208-05-25' % name)  # 被装饰的函数带参数的情况

for i in range(10):
    today()
print(today.count)  # 10