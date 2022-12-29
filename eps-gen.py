#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randrange
import re
import sys

consonants = \
{
        'ʔ': 20,
        'p': 6,
        't': 15,
        'k': 15,
        'r': 7,
        'l': 10,
        'n': 15,
        'y': 4,
        'w': 4,
        'G': 4,
        '': 50,
}

vowels = \
{
        'a': 50,
        'i': 50,
        'u': 40,
}

affixes = \
{
        'ʔ': 15,
        'p': 4,
        't': 15,
        'k': 15,
        'r': 12,
        'l': 10,
        'n': 12,
        'y': 4,
        'w': 4,
        'G': 4,
        'a': 10,
        'i': 10,
        'u': 7,
}

word = ''

def select(l):
        a = randrange(sum(l.values()))
        for k in l.keys():
                if a < l[k]:
                        return k
                a -= l[k]

if len(sys.argv) > 1 and sys.argv[1] == 'affix':
    word += select(affixes)
    if (randrange(10) < 8): 
        word += select(affixes)
    print(word)
    exit(0)

def add_consonant():
    x = select(consonants)
    if (len(x) > 0 and randrange(10) < 5): x += 'ʲ'
    return x

word += add_consonant()
word += add_consonant()
word += select(vowels)
word += add_consonant()
word += add_consonant()

if (randrange(10) < 5):
    word += add_consonant()
    word += select(vowels)
    word += add_consonant()
    word += add_consonant()

print(word)

print(word)
