def double(func):
    def wrapper():
        func()
        func()
    return wrapper

@double
def test():
    print("Does it work?")
