def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
    print()

foo('hello')
foo('hello', 1, 2)
foo('hello', 1, 2, key1='key', key2='key2')

