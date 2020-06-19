import functools


def new_logging_tool(obj):
    if isinstanc(obj, str):  # 带参数的情况，参数类型为str
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*arg, **kwargs):
                if obj == 'error':
                    print('%s is running...' % func.__name__)
                elif obj == 'warn':
                    print('%s is running...' % func.__name__)
                else:
                    print('%s is running...' % func.__name__)
                func()
            return wrapper
        return decorator
    else:  # 不带参数的情况，参数类型为函数类型，即被装饰的函数
        @functools.wraps(obj)
        def wrapper(*args, **kwargs):
            print('%s is running...' % obj.__name__)
            obj()
        return wrapper

@new_logging_tool
def yesterday():
    print('2018-05-24')

yesterday()

@new_logging_tool('warn')
def today(name='devin'):
    print('Hello, %s! Today is 208-05-25' % name)

today()