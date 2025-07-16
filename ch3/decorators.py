def uppercase(func):
    def wrapper():
        orig_res = func()
        modif_res = orig_res.upper()
        return modif_res
    return wrapper

@uppercase
def greet1():
    return 'Hello!'
print(greet1())


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet2():
    return "Hello!"
print(greet2())


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'ТРАССИРОВКА: вызвана {func.__name__}() c {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'ТРАССИРОВКА: {func.__name__}() вернула {original_result!r}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'
print(say('Djane', 'Hello world!'))


import functools

def uppercase2(func):

    @functools.wraps(func)
    def wrapper():
        return func().upper()

    return wrapper

@uppercase2
def greet3():
    '''Вернуть приветсвие.'''
    return 'Hello!'
print(greet3.__name__)
print(greet3.__doc__)
