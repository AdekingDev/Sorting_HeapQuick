import random

def heapify(arr, n, i, counter):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        counter[0] += 1
        heapify(arr, n, largest, counter)

def heapSort(arr):
    counter = [0]
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, counter)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        counter[0] += 1
        heapify(arr, i, 0, counter)

    return counter[0]

def partition(arr, low, high, counter):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            counter[0] += 1

    arr[i+1], arr[high] = arr[high], arr[i+1]
    counter[0] += 1
    return (i+1)

def quickSort(arr, low, high, counter):
    if low < high:
        pi = partition(arr, low, high, counter)

        quickSort(arr, low, pi-1, counter)
        quickSort(arr, pi+1, high, counter)

#random array of 100 integers
array = [random.randint(0, 1000) for _ in range(100)]

array_for_quick_sort = array.copy()

# Sorting using heap sort and quick sort
heap_sort_operations = heapSort(array)
quick_sort_operations = [0]
quickSort(array_for_quick_sort, 0, len(array_for_quick_sort) - 1, quick_sort_operations)
heap_sort_operations, quick_sort_operations[0], array == array_for_quick_sort

print("Array after sorting with Heap Sort: \n", array)
print("Number of operations in Heap Sort:", heap_sort_operations)

print("\nArray after sorting with Quick Sort: \n", array_for_quick_sort)
print("Number of operations in Quick Sort:", quick_sort_operations[0])

print("\nAre there any difference in numer of operations?", array == array_for_quick_sort)
