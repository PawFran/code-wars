def next_bigger(n):
    lst = list(str(n))
    print lst
    for i in range(len(lst)):
        current_idx = len(lst) - 1 - i
        if lst[current_idx] > lst[current_idx - 1] and current_idx > 0:
            # find index of the smallest number to the right which would still be greater than value at current_idx - 1
            min_val = min(j for j in lst[current_idx:] if j > lst[current_idx - 1])
            min_idx = lst[current_idx:].index(min_val) + current_idx
            # swap
            lst[min_idx], lst[current_idx - 1] = lst[current_idx - 1], lst[min_idx]
            # sort right side
            lst = lst[:current_idx] + sorted(lst[current_idx:])

            return int(''.join(lst))

    return -1

print next_bigger(2017)
print next_bigger(2780)
print next_bigger(234567891)
print next_bigger(2)
print next_bigger(222)
print next_bigger(531)
print next_bigger(59853)

# list=[1.1412, 4.3453, 5.8709, 0.1314]
# print list.index(min(list))