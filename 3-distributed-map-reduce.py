#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
    Distribute work out to Pool workers for reduction steps.
    Allows for parallel processing of word counts.
"""
# Imports.
from    multiprocessing import Pool
from    common          import my_cmp
import  json
import  timeit


# Setup.
def _map():
    """
        Return the word list that we're working from.

        These are partitioned into segments based off of their first
        letter, for easier processing by the reducers.
    """
    partitions = {
        'ab': [],
        'cd': [],
        'ef': [],
        'gh': [],
        'ij': [],
        'kl': [],
        'mn': [],
        'op': [],
        'qr': [],
        'st': [],
        'uv': [],
        'wx': [],
        'yz': [],
    }
    thesewords = open('./words', 'r')

    def map_step(a):
        """
            Partition off as needed.
        """
        if not a:
            return

        for key in partitions:
            if a[0] in key:
                # Append and remove the trailing newline.
                partitions[key].append(a[:-1])
                break

    map(map_step, thesewords)

    # Sort the words in the partition before they're sent out.
    for key in partitions:
        partitions[key] = sorted(partitions[key])

    return partitions


# Reduction step 1.
def _reduce_step_1(a):
    """
        Given a list of words from a particular partition, generate a
        list of top 5 words.

        These can be run in parallel.
    """
    result = reduce(_inner_reduce_step_1, a[1], {})
    # The reduce step will still have the last word it looked at,
    # whether or not it should be included.
    # We must ensure it is removed here.
    return (a[0], sorted(result.iteritems(),
        key=my_cmp, reverse=True)[:5])


def _inner_reduce_step_1(a, b):
    """
        Keep a running top-5 total for this wordlist partition.
    """
    if b not in a:
        if len(a) > 5:
            a = dict(sorted(a.iteritems(),
                key=my_cmp, reverse=True)[:5])

        a[b] = 1
    else:
        a[b] += 1

    return a



def _main():
    """
        Timed script.
    """
    tops = {}

    def calculate_tops(a):
        """
            Put the top 5 results in their right place.
        """
        for group in a:
            for word in group[1]:
                tops[word[0]] = word[1]

    words           = _map()
    process_pool    = Pool(processes=13)
    results = process_pool.map_async(_reduce_step_1,
        words.iteritems(), callback=calculate_tops)

    results.wait()
    print json.dumps(sorted(tops.iteritems(), key=my_cmp,
        reverse=True)[:5])

if __name__ == '__main__':
    print "Distributed reducers approach:"
    print timeit.timeit('_main()', setup='from __main__ import _main', number=1)
    print ""
