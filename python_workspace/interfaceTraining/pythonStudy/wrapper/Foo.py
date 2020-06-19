class Foo(object):
    def __init__(self, func):
        self._func = func  # 初始化装饰的函数

    def __call__(self):
        print ('class decorator runing')
        self._func()  # 调用装饰的函数
        print ('class decorator ending')

@Foo
def bar():  # 被装饰函数不带参数的情况
    print ('bar')

bar()