def mix(x, y):
    x_new = [item for item in x for i in range(len(y))]
    y_new = y * len(x)
    res = []
    for i in range(len(x_new)):
        try:
            tmp = [item for item in x_new[i]]
            tmp.append(y_new[i])
            res.append(tmp)
        except:
            res.append([x_new[i], y_new[i]])

    return res

def get_pins(observed):
    d = {'1': ['1', '2', '4'], '2': ['1', '2', '3', '5'], '3': ['2', '3', '6'], '4': ['1', '4', '5', '7'],
         '5': ['2', '4', '5', '6', '8'], '6': ['3', '5', '6', '9'], '7': ['4', '7', '8'],
         '8': ['5', '7', '8', '9', '0'],
         '9': ['6', '8', '9'], '0': ['8', '0']}
    lst = [d[item] for item in observed]

    res = lst[0]
    for i in range(1, len(lst)):
        res = mix(res, lst[i])

    return [''.join(item) for item in res]

print get_pins('1357')
