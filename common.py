#!/usr/bin/env python2.7
"""
    Common functions all the methods use.
"""
# Setup.
__thesewords = open('./words', 'r')
words = __thesewords.read().split('\n')


# Compare two values by value, and then by key first letter.
def my_cmp(x):
    """
        Comparison of values in word lists.

        Will prefer later letters in the alphabet, due to how sorting
        works. Might swap values.
    """
    if x[0]:
        return "%s%s" % (x[1], x[0])
