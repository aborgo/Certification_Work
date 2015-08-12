"""
Simplest example of creating a decorator,
adds arbitrary arguments to any decorated function.
"""

def addarg(item):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(item, *args, **kwargs)
        return wrapper
    return decorator
