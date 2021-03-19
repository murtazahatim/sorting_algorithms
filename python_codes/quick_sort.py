def quick_sort(lst):
    aux_quick_sort(lst, 0, len(lst) - 1)
    return lst


def aux_quick_sort(lst, start, end):
    if start >= end:
        return
    pivot_pos = partition(lst, start, end)
    aux_quick_sort(lst, start, pivot_pos - 1)
    aux_quick_sort(lst, pivot_pos + 1, end)


def partition(lst, start, end):
    pivot = lst[start]
    low, high = start + 1, end

    while True:
        while low <= high and lst[low] <= pivot:
            low += 1

        while low <= high and lst[high] >= pivot:
            high -= 1

        if low <= high:
            lst[low], lst[high] = lst[high], lst[low]
        else:
            break

    lst[start], lst[high] = lst[high], lst[start]
    return high
