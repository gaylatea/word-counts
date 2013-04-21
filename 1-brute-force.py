#!/usr/bin/env python2.7
"""
    Provide a count of the top 5 words in a given word list.
"""
# Imports.
from    common import words, my_cmp
import  json
import  timeit


# Collection.
def _main():
    """
        Very simple brute-force solution to this one.
    """
    counts = {}
    for each in words:
        if each not in counts:
            counts[each] = 1
        else:
            counts[each] += 1

    # Sort the output.
    print json.dumps(sorted(counts.iteritems(), key=my_cmp,
        reverse=True)[:5])

if __name__ == '__main__':
    print "Brute-force approach:"
    print timeit.timeit('_main()', setup='from __main__ import _main', number=1)
    print ""
