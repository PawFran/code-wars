def openOrSenior(data):
    res = []
    for lst in data:
        if lst[0] >= 55 & lst[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    return res

print openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]])