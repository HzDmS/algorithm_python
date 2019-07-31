""" Python implementation of mergeSort. """

import random
import time


def merge(arr, low, mid, high):

    """ in-place merge

    Parameters
    ----------
    arr: list
    low: int, index of the first element.
    mid: int, index of the middle element.
    high: int, index of the last element.

    """

    left = arr[low: mid + 1]
    right = arr[mid + 1: high + 1]

    i, j, k = 0, 0, low
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):

    """ in-place merge sort

    Parameters
    ----------
    arr: list
    low: int, index of the first element.
    high: int, index of the last element.

    """

    if low >= high:
        return
    mid = low + (high - low) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    merge(arr, low, mid, high)


if __name__ == "__main__":

    arr = [random.randint(0, 1000) for _ in range(int(1e4))]

    start = time.time()
    merge_sort(arr, 0, len(arr) - 1)
    end = time.time()
    print("total time: {:3f}".format(end - start))
