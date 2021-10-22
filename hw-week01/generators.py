def meow_generator():
    x = "Meow"
    while True:
        yield x
        x = x + " " + x

g = meow_generator()
print([next(g) for i in range(10)])
