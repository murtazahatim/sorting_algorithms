from math import floor, log


def radix_sort(lst):
    max_num = max(lst)
    num_of_digits = 1 + floor(log(max_num, 10))

    counter = 1

    while counter <= num_of_digits:
        lst = counting_sort(lst, counter)
        counter += 1

    return lst


def counting_sort(lst, counter):
    count = [0] * 10
    position = [0] * 10

    for elem in lst:
        if counter > (1 + floor(log(elem, 10))):
            count[0] += 1
        else:
            count[(elem % (10**counter))//(10**(counter - 1))] += 1

    for i in range(1, len(count)):
        position[i] = count[i-1] + position[i-1]

    res = [None] * len(lst)

    for elem in lst:
        res[position[(elem % (10**counter))//(10**(counter - 1))]] = elem
        position[(elem % (10**counter))//(10**(counter - 1))] += 1

    return res
