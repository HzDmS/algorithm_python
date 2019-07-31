""" Heapsort. """


def left(x):

    """ Return index left child of node x.

    Parameters
    ----------
    x: int, index.

    Returns
    -------
    int, index of left child.

    """

    return x * 2


def right(x):

    """ Return index right child of node x.

    Parameters
    ----------
    x: int, index.

    Returns
    -------
    int, index of right child.

    """

    return x * 2 + 1


def max_heapify(arr, root, end):

    """ Max_heapify a list in place.

    Parameters
    ----------
    arr: list
    x: int, index of root.
    end: int, index of last element.

    """

    l_idx = left(root)
    r_idx = right(root)

    largest = root

    if l_idx <= end and arr[l_idx] > arr[largest]:
        largest = l_idx
    if r_idx <= end and arr[r_idx] > arr[largest]:
        largest = r_idx
    if not largest == root:
        arr[largest], arr[root] = arr[root], arr[largest]
        max_heapify(arr, largest, end)


def build_max_heap(arr):

    """ Build a max heap.

    Parameters
    ----------
    arr: list

    """

    n = len(arr)

    for i in range((n - 1) // 2, -1, -1):
        max_heapify(arr, i, n - 1)


def heapsort(arr):

    """ Heapsort.

    Parameters
    ----------
    arr: list.

    """

    n = len(arr)
    build_max_heap(arr)
    print(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0, i - 1)


if __name__ == "__main__":

    arr = [*range(10)]
    heapsort(arr)
    print(arr)
