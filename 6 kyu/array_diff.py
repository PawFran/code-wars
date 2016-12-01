def array_diff(a, b):
    return filter(lambda n: n not in b, a)

print type(array_diff([1,2], [1]))