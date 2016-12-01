def order_weight(strng):
    return ' '.join(sorted(strng.split(" "), key = lambda x: (sum(map(int, x)), x)))

print order_weight("103 123 4444 99 2000")
print order_weight("71899703 200 6 91 425 4 67407 7 96488 6 4 2 7 31064 9 7920 1 34608557 27 72 18 81")

def order_weight2(strng):
    lst = strng.split(" ")
    lst = [map(int, el) for el in lst] # returns list of lists of ints
    lst = sorted(lst, key = lambda x: (sum(x), ''.join(map(str, x))))
    lst = [''.join(map(str, el)) for el in lst]

    return ' '.join(lst)