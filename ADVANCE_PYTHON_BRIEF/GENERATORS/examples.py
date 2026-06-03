basic generator-
def count():
    yield 1
    yield 2
    yield 3

for num in count():
    print(num)


generator loop-
def even_numbers():
    num = 0

    while True:
        yield num
        num += 2

g = even_numbers()

for _ in range(5):
    print(next(g))
