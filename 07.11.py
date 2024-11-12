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
        print(f"Execution time: {end_time - start_time:.2f} second")
        return result
    return wrapper
@timing
def slow_function():
    time.sleep(1)
    return "Done!"
slow_function()
#4
def check_permissions(user_permissions):
    def requires_permission(permission):
        def decorator(func):
            def wrapper(*args, **kwargs):
                if permission in user_permissions:
                    return func(*args, **kwargs)
                raise PermissionError('Permission Denied at line:', 157)
            return wrapper
        return decorator
    return requires_permission
user_permissions = ["user", "admin"]
@check_permissions(user_permissions)("admin")
def delete_user(user_id):
    return f"User {user_id} deleted."
print(delete_user(42))