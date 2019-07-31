""" KMP implementation """

def compute_prefix(pattern) -> list:
    """ Compute prefix list of pattern 
    
    Parameters
    ----------
    pattern: str, target pattern

    Returns
    -------
    prefix: list

    """

    l_pattern = len(pattern)
    prefix = [0] * l_pattern

    for i in range(1, l_pattern):

        k = prefix[i - 1]

        while k > 0 and not pattern[k] == pattern[i]:
            k = prefix[k - 1]
        if pattern[k] == pattern[i]:
            k += 1
        prefix[i] = k
    
    return prefix


def search(text, pattern) -> list:
    """ Search pattern in text
    
    Parameters
    ----------
    text: str, input text.
    pattern: str, target pattern.

    Returns
    -------
    list, occurrence of pattern in text.
    """

    l_text, l_pattern = len(text), len(pattern)
    prefix = compute_prefix(pattern)
    positions, j = [], 0

    for i in range(l_text - l_pattern + 1):
        while j > 0 and not pattern[j] == text[i]:
            j = prefix[j - 1]
        if pattern[j] == text[i]:
            j += 1
        if j == l_pattern:
            positions.append(i - l_pattern + 1)
            j = prefix[j - 1]

    return positions


if __name__ == "__main__":

    text = "aadsadsaaaaaacaglaaaaslkdaaaaaskdjabaaaaaadsaaaasdasd"
    pattern = "aaaa"
    positions = search(text, pattern)
    if len(positions):
        print("Found pattern '{:s}' at position {}".format(
            pattern, positions))
        for i in positions:
            print(text[i:i + len(pattern)])
    else:
        print("Not found!")



