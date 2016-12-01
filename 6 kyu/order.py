import re

def order(sentence):
    if not sentence:
        return ''
    s = sentence.split()
    lst = [None] * len(s)
    for word in s:
        n = (int)(re.findall('[1-9]', word)[0])
        lst[n - 1] = word
    return ' '.join(lst)

print order("is2 Thi1s T4est 3a")