def counting_sort(lst):
    count_arr = [0] * (max(lst) + 1)
    position_arr = [0] * (max(lst) + 1)
    res = [None] * len(lst)

    for elem in lst:
        count_arr[elem] += 1

    for ind in range(2, len(count_arr)):
        position_arr[ind] = count_arr[ind-1] + position_arr[ind-1]

    for elem in lst:
        res[position_arr[elem]] = elem
        position_arr[elem] += 1

    return res

