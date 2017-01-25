from src import alignment


def naive_overlap(a: str, b: str, print_alignment=False) -> int:
    """
    Naive overlap method. It compares each prefix/suffix pair of equal length of a and b to compute the overlap between them.
    Example: a = 'bbaaa', b = 'aaabbb', score_only=False
    Output: Score: 3
            bbaaa---
              |||
            --aaabbb

    :param a: first string
    :param b: second string
    :param print_alignment: if true it prints the overlapping strings and the resulting score
    :return: overlap score
    """
    max_score = 0
    for k in range(min(len(a), len(b)), 0, -1):
        if a[-k:] == b[:k]:
            max_score = k
            break
    if print_alignment:
        print('Score: {}'.format(max_score))
        print(a + (len(b) - max_score) * '-')
        print((len(a) - max_score) * ' ' + max_score * "|" + (len(b) - max_score) * ' ')
        print((len(a) - max_score) * '-' + b)
    return max_score


def overlap(a: str, b: str, print_alignment=False) -> int:
    """
    Overlap method. Uses the general alignment method with a special alignment configuration
    (mismatch = gap_open = gap_extend = -(len(a) + len(b)), left = bottom = True).
    Example: a = 'bbaaa', b = 'aaabbb', score_only=False
    Output: Score: 3
            bbaaa---
              |||
            --aaabbb

    :param a: first string
    :param b: second string
    :param print_alignment: if true it prints the overlapping strings and the resulting score
    :return: overlap score
    """
    mismatch = gap_open = gap_extend = -(len(a) + len(b))
    left = bottom = True
    return alignment.align(a, b, print_alignment=print_alignment, mismatch=mismatch, gap_open=gap_open,
                           gap_extend=gap_extend, left=left, bottom=bottom)
