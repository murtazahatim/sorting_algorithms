def heap_sort(lst):
    heap_lst = [None] * (len(lst) + 1)

    for ind in range(len(lst)):
        heap_lst[ind + 1] = lst[ind]

    length = len(heap_lst)
    for n in range(length - 1, 1, -1):
        heap_lst[:n+1] = heapify(heap_lst[:n + 1])
        heap_lst[1], heap_lst[n] = heap_lst[n], heap_lst[1]

    return heap_lst[1:]


def heapify(lst):
    k = (len(lst) - 1) // 2
    while k > 0:
        sink(lst, k)
        k -= 1
    return lst


def sink(lst, k):
    while 2*k < len(lst):
        larger_child = largest_child(k, lst)
        if lst[k] < lst[larger_child]:
            lst[k], lst[larger_child] = lst[larger_child], lst[k]
        else:
            break


def largest_child(k, lst):
    if 2*k == len(lst) - 1:
        return 2*k
    elif lst[2*k] > lst[2*k + 1]:
        return 2*k
    else:
        return 2*k + 1
