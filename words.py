#!/usr/bin/env python2.7
"""
    Provide a count of the top 5 words in a given word list.
"""
# Imports.
import operator
import timeit

# Setup.
thesewords = open('./words', 'r')
words = thesewords.read().split('\n')


# Collection.
def _brute_force_v1():
    """
        Very simple brute-force solution (slow) to this one.
    """
    counts = {}
    for each in words:
        if each not in counts:
            counts[each] = 1
        else:
            counts[each] += 1

    # Sort the output.
    for each in sorted(
        counts.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]:
        print "%s: %s" % (each[0], each[1])


def _remove_list_v2():
    """
        Count ahead of time and remove words to shorten processing.
    """
    tempwords = words
    counts = {}
    while True:
        # Compute out how many occurrences we see of each word.
        if not tempwords:
            break

        current_word = tempwords.pop()
        count = len([x for x in tempwords if x == current_word])
        counts[current_word] = count

        tempwords = [x for x in tempwords if x != current_word]

    # Sort the output.
    for each in sorted(
        counts.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]:
        print "%s: %s" % (each[0], each[1])

if __name__ == '__main__':
    print "Brute-force approach:"
    print timeit.timeit('_brute_force_v1()', setup='from __main__ import _brute_force_v1', number=1)
    print ""
    print "List-delete approach:"
    print timeit.timeit('_remove_list_v2()', setup='from __main__ import _remove_list_v2', number=1)
