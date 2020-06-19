def logging_tool(func):
    def wrapper(*arg, **kwargs):
        print('%s is running...' % func.__name__)
        func()  # 把today当作参数传递进来，执行func()就相当于执行today()
    return wrapper

@logging_tool
def today():
    print('2018-05-25')

today()