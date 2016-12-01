def validateBattlefield(field):
    count = [0] * 4


    for row in range(len(field)):
        for col in range(len(field)):
            if field[row][col] == 1:
                pass

lst = [1, 0, 0, 0, 0, 1, 1, 0, 0, 0]
current = 5
# count ones from current
try:
    idx = lst.index(0, current)
    size = idx - current
except ValueError:
    size = 1

print size


    # print count
    # print count == [4, 3, 2, 1]




battleField =   [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

validateBattlefield(battleField)