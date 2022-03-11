def func_counter(func):
    def wrapper(arg):
        wrapper.counter += 1
        return func(arg)
    wrapper.counter = 0
    return wrapper
