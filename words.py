#!/usr/bin/env python2.7
"""
    Provide a count of the top 5 words in a given word list.
"""
# Imports.
import json
import timeit

# Setup.
thesewords = open('./words', 'r')
words = thesewords.read().split('\n')

# Compare two values by value, and then by key first letter.
def _my_cmp(x):
    """
        Comparison of values in word lists.

        Will prefer later letters in the alphabet, due to how sorting
        works. Might swap values.
    """
    if x[0]:
        return "%s%s" % (x[1], x[0])


# Collection.
def _brute_force_v1():
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
    print json.dumps(sorted(counts.iteritems(), key=_my_cmp,
        reverse=True)[:5])


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
    print json.dumps(sorted(counts.iteritems(), key=_my_cmp,
        reverse=True)[:5])


def _map_reduce_v3():
    """
        Try map/reduce to count more efficiently.
        Slower, but doesn't keep a giant dictionary in memory.

        Still requires the words from the load state in mem, though.

        What worries me is that this really requires the inputs be
        sorted, otherwise it cannot function properly.

        This means that it cannot be done in parallel with the map
        step, which would make processing with a big Map/Reduce system
        a little trickier.
    """
    s = sorted(words)


    def reduce_step(a, b):
        """
            Keep a running top-5 total for the wordlist.
            The "top-5" is stored as a dict of dict[word] = count
        """
        # Ensure that after processing of each one is done you
        # drop the dict down to 5 entries.
        if b not in a:
            if len(a) > 5:
                a = dict(sorted(a.iteritems(),
                    key=_my_cmp, reverse=True)[:5])

            a[b] = 1
        else:
            a[b] += 1

        return a

    # The reduce engine will actually return the last item additionally,
    # so we need to remove it.
    result = reduce(reduce_step, s, {})
    print json.dumps(sorted(result.iteritems(), key=_my_cmp,
        reverse=True)[:5])

if __name__ == '__main__':
    print "Brute-force approach:"
    print timeit.timeit('_brute_force_v1()', setup='from __main__ import _brute_force_v1', number=1)
    print ""
    print "Map-reduce approach:"
    print timeit.timeit('_map_reduce_v3()', setup='from __main__ import _map_reduce_v3', number=1)
    print ""
