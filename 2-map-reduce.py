#!/usr/bin/env python2.7
"""
    Serial reducer engine.
"""
# Imports
from    common import words, my_cmp
import  json
import  timeit

def _main():
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
                    key=my_cmp, reverse=True)[:5])

            a[b] = 1
        else:
            a[b] += 1

        return a

    # The reduce engine will actually return the last item additionally,
    # so we need to remove it.
    result = reduce(reduce_step, s, {})
    print json.dumps(sorted(result.iteritems(), key=my_cmp,
        reverse=True)[:5])

if __name__ == '__main__':
    print timeit.timeit('_main()', setup='from __main__ import _main', number=1)
    print ""
