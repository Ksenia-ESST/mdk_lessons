#1 
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper
@uppercase
def greet(name):
    return f"Hello, sanches, {name}"
print(greet("Senya"))
#2
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return ' '.join(func(*args, **kwargs)for _ in range(n))
        return wrapper
    return decorator
@repeat(10)
def say_hello():
    return "Hello!"
print(say_hello())
#3
import time
def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.3f} second")
        return result
    return wrapper
@timing
def slow_function():
    time.sleep(3)
    return "Done!"
slow_function()