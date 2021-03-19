def merge_sort(lst):
    if len(lst) == 1:
        return lst
    lst1 = merge_sort(lst[:len(lst)//2])
    lst2 = merge_sort(lst[len(lst)//2:])

    return merge(lst1, lst2)


def merge(lst1, lst2):
    res = []

    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1

    if i >= len(lst1):
        res.extend(lst2[j:])
    elif j >= len(lst2):
        res.extend(lst1[i:])

    return res
