#!/usr/bin/env python2.7
"""
    Common functions all the methods use.
"""
# Setup.
words = open('./words', 'r')


# Compare two values by value, and then by key first letter.
def my_cmp(x):
    """
        Comparison of values in word lists.

        Will prefer later letters in the alphabet, due to how sorting
        works. Might swap values.
    """
    if x[0]:
        return  x[1]


def mysort(a):
    """
        Sort the list of words as quickly as possible.
    """
    result = []
    for each in a:
        if not result:
            result.append(each)
            continue

        result = result[:5]
        if len(result) == 5:
            if result[-1][1] >= each[1]:
                continue

        for pos, res in enumerate(result):
            if each[1] >= res[1]:
                result.insert(pos, each)
                break

        result.append(each)

    return result[:5]

