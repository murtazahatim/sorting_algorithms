def insertion_sort(lst):
    for i in range(1, len(lst)):
        for k in range(i, 0, -1):
            if lst[k-1] > lst[k]:
                lst[k - 1], lst[k] = lst[k], lst[k - 1]
            else:
                break
    return lst