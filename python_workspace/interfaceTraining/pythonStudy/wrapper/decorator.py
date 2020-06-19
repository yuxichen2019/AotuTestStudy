def logging_tool(level):
    def decorator(func):
        def wrapper(*arg, **kwargs):
            if level == 'error':
                print('%s is running...' % func.__name__)
            elif level == 'warn':
                print('%s is running...' % func.__name__)
            else:
                print('%s is running...' % func.__name__)
            func()
        return wrapper
    return decorator

@logging_tool(level='warn')
def today(name='devin'):
    print('Hello, %s! Today is 208-05-25' % name)

today()