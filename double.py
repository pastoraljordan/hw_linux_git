def doubler(func):
    def wrapper():
        func()
        func()
    return wrapper

@doubler
def test():
    print("Does it work?")
