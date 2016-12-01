def accum(s):
    lst = []
    counter = 1
    for c in s:
        for i in range(counter):
            lst.append(c.lower())
        lst.append('-')
        counter = counter + 1
    lst.pop()
    lst[0] = lst[0].upper()
    for i in range(1, len(lst)):
        if lst[i - 1] == '-':
            lst[i] = lst[i].upper()
    return ''.join(lst)

print accum("ZpglnRxqenU")