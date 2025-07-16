from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        f = open(name, 'r')
        yield f
    finally:
        f.close()


with managed_file('hello.txt') as f:
    f.write('Hello')
    f.write('world!')
