import random
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from counting_sort import counting_sort
from radix_sort import radix_sort


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

lst = generate_random_list(100)

print('Merge Sort: ' + str(merge_sort(lst)))

lst = generate_random_list(100)

print('Quick Sort: ' + str(quick_sort(lst)))

lst = generate_random_list(100)

print('Heap Sort: ' + str(heap_sort(lst)))

lst = generate_random_list(100)

print('Counting Sort: ' + str(counting_sort(lst)))

lst = generate_random_list(100)

print('Radix Sort: ' + str(radix_sort(lst)))
