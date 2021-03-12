import random
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort


def generate_random_list(length):
    start = 5
    stop = 500
    return [random.randint(start, stop) for _ in range(length)]


lst = generate_random_list(100)

print('Bubble Sort: ' + str(bubble_sort(lst)))

lst = generate_random_list(100)

print('Selection Sort: ' + str(selection_sort(lst)))

lst = generate_random_list(100)

print('Insertion Sort: ' + str(insertion_sort(lst)))
