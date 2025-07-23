class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


repeater = Repeater('Hello!')
for i in repeater:
    print(i)


# repeater = Repeater('Hello!')
# iterator = repeater.__iter__()
# while True:
#     item = iterator.__next__()
#     print(item)

iterator = iter(repeater)
next(iterator)


class BoundedRepeater:
    def __init__(self, value, max_reps):
        self.value = value
        self.max_repeats = max_reps
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

repeater = BoundedRepeater('Message', 5)
for i in repeater:
    print(i)

repeater = BoundedRepeater('Привет', 3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)
