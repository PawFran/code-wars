def make_readable(seconds):
    s = str(seconds % 60)
    m = str((seconds / 60) % 60)
    h = str((seconds / 3600) % 100)
    if len(s) == 1:
        s = "0" + s
    if len(m) == 1:
        m = "0" + m
    if len(h) == 1:
        h = "0" + h

    return ":".join([h, m, s])

print make_readable(86399)

# other solutions
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
