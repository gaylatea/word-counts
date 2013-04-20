#!/usr/bin/env python2.7
"""
    Provide a count of the top 5 words in a given word list.
"""
# Imports.
import operator
import timeit
import resource

# Setup.
thesewords = open('./words', 'r')
words = thesewords.read().split('\n')


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


def _map_reduce_v3():
    """
        Try map/reduce to count more efficiently.
        Slower, but doesn't keep a giant dictionary in memory.

        Still requires the words from the load state in mem, though.
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
                    key=operator.itemgetter(1), reverse=True)[:5])

            a[b] = 1
        else:
            a[b] += 1

        return a

    # The reduce engine will actually return the last item additionally,
    # so we need to remove it.
    result = reduce(reduce_step, s, {})
    for each in sorted(result.iteritems(), key=operator.itemgetter(1),
        reverse=True)[:5]:
        print "%s: %s" % (each[0], each[1])

if __name__ == '__main__':
    print "Brute-force approach:"
    print timeit.timeit('_brute_force_v1()', setup='from __main__ import _brute_force_v1', number=1)
    run_1_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print "%s kB" % (run_1_rss / 1024 / 1024)
    print ""
    print "Map-reduce approach:"
    print timeit.timeit('_map_reduce_v3()', setup='from __main__ import _map_reduce_v3', number=1)
    run_3_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if run_3_rss == run_1_rss:
        print "Uses less memory!"
    print ""
