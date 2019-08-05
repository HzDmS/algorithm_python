# Brute-force solution


def search(text, pattern) -> list:
    """ Search pattern in text.

    Parameters
    ----------
    text: str, input text.
    pattern: str, target pattern.

    Returns
    -------
    List, position of the first character if found, else \
        the length of text.
    """

    n, m = len(text), len(pattern)
    positions = []

    for i in range(n - m + 1):
        j = 0
        while j < m:
            if not text[i + j] == pattern[j]:
                break
            j += 1
        if j == m:
            positions.append(i)
    return positions


if __name__ == "__main__":

    text = "aadsadsfasdasdgdfglkljdflaslkdjlfkajlskdjfladsdadasdasd"
    pattern = "this"
    positions = search(text, pattern)
    if len(positions):
        print("Found pattern '{:s}' at position {}".format(
            pattern, positions))
        for i in positions:
            print(text[i:i + len(pattern)])
    else:
        print("Not found!")
