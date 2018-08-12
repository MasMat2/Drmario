
def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element


iterable = cycle(('a', 'b', 'c'))
for i in range(100):
    print(next(iterable), i)
