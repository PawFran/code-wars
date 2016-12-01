def find_even_index(arr):
    left = 0
    right = sum(arr[1:])
    if left == right:
        return 0
    for i in range(1, len(arr)):
        left += arr[i - 1]
        right -= arr[i]
        if left == right:
            return i

    return -1

# other solutions
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

def find_even_index(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1