# counting sort

import random


def counting_sort(arr):
    """ Counting sort.

    time complexity: O(n + k)
    space complexity: O(n + k)

    Parameters
    ----------
    arr: list of positive int.
    """

    n, k = len(arr), max(arr)
    counting = [0] * (k + 1)
    res = [0] * n

    for i in range(n):
        counting[arr[i]] += 1

    for i in range(1, k + 1, 1):
        counting[i] = counting[i - 1] + counting[i]

    for i in range(n - 1, -1, -1):
        res[counting[arr[i]] - 1] = arr[i]
        counting[arr[i]] -= 1

    return res


if __name__ == "__main__":

    k = 10000
    n = 100
    arr = [random.randint(0, k) for _ in range(n)]
    print(counting_sort(arr))
