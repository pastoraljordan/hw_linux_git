import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Total time {end - start} seconds')
    return wrapper

@calculate_time
def countdown():
    x = 100000000
    print("test")
    while x > 0:
        x = x - 1
