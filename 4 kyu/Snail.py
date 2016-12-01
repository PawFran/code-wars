def moveDown(array, lst,  start_i, start_j, steps):
    for k in range(steps):
        lst.append(array[start_i + k][start_j])

def moveLeft(array, lst,  start_i, start_j, steps):
    for k in range(steps):
        lst.append(array[start_i][start_j - k])

def moveUp(array, lst,  start_i, start_j, steps):
    for k in range(steps):
        lst.append(array[start_i - k][start_j])

def moveRight(array, lst,  start_i, start_j, steps):
    for k in range(steps):
        lst.append(array[start_i][start_j] + k)

def snail(array):
    n = len(array[0])
    lst = []
    steps = n
    moveRight(array, lst, 0, 0, steps)
    for k in range(n):
        steps -= 1
        moveDown(array, lst, k + 1, n - 1 - k, steps)
        moveLeft(array, lst, n - 1 - k, n - 2 - k, steps)

        steps -= 1
        moveUp(array, lst, n - 2 - k, k, steps)
        moveRight(array, lst, k + 1, k + 1, steps)

    return lst


# other solutions
def snail2(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []

array = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

print snail(array)
