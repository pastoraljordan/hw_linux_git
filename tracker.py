def func_counter(func):
    def wrapper(arg):
        wrapper.counter += 1
        return func(arg)
    wrapper.counter = 0
    return wrapper


@func_counter
def foo(y):
    return y + 2 ** 3 - 34


foo(1)
foo(1)
print(foo.counter)

