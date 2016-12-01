def find_missing(sequence):
    diff = min(abs(sequence[1] - sequence[0]), abs(sequence[2] - sequence[1])) * cmp(sequence[1], sequence[0])
    for i in range(len(sequence)):
        if sequence[i] != sequence[0] + diff * i:
            return sequence[i - 1] + diff


print find_missing([1, 2, 3, 4, 6, 7, 8, 9])


# other solutions
def find_missing2(sequence):
    interval = (sequence[-1] - sequence[0])/len(sequence)
    for previous, item in enumerate(sequence[1:]):
        if item - sequence[previous] != interval:
            return item - interval