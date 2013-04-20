#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
    Distribute work out to Pool workers for reduction steps.
    Allows for parallel processing of word counts.
"""
# Imports.
import operator
import timeit

# Setup.
# Should investigate setting this up properly during the map() phase.
thesewords = open('./words', 'r')
words = thesewords.read().split('\n')

# Reduction step 1.
def _reduce_step_1(a, b):
    """
        Given a list of words from a particular partition, generate a
        list of top 5 words.

        These can be run in parallel.
    """
    pass


def _reduction_step_2(a, b):
    """
        Given dicts of {<word>: <count>, ...}, generate the final count
        of top 5 words.

        Investigate running this in parallel too.
    """
    pass


def _main():
    """
        Timed script.
    """
    pass

if __name__ == '__main__':
    print "Distributed reducers approach:"
    print timeit.timeit('_main', setup='from __main__ import _main', number=1)
    print ""
