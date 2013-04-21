#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
    Generate a random word list for use in the word count script.
"""
# Imports.
import random

# Generation.
def _main():
    """
        Generate the actual list and write it out.
    """
    systemwords = open('/usr/share/dict/words', 'r')
    thesewords  = open('./words', 'w')

    words = systemwords.read().split('\n')

    new_words = []
    required_words = 1000000
    for x in xrange(0, required_words):
        new_words.append(random.choice(words))

    output = '\n'.join(new_words)
    thesewords.write(output)

if __name__ == '__main__':
    exit(_main())
