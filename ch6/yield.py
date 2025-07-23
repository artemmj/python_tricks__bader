def repeater(value):
    while True:
        yield value


def bounded_repeater(value, max_reps):
    for _ in range(max_reps):
        yield value


def integers():
    for i in range(0, 10):
        yield i


def squared(seq):
    for i in seq:
        yield i * i


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squared(integers()))
