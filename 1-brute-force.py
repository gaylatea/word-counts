#!/usr/bin/env python2.7
"""
    Provide a count of the top 5 words in a given word list.
"""
# Imports.
from    common import words, mysort
from operator import itemgetter
import  json
import  timeit


# Collection.
def _main():
    """
        Very simple brute-force solution to this one.
    """
    counts = {}
    for each in words:
        each = each[:-1]
        if each not in counts:
            counts[each] = 1
        else:
            counts[each] += 1

    # Sort the output.
    print mysort(counts.iteritems())

if __name__ == '__main__':
    _main()
