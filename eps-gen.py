#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randrange
import re
import sys

consonants = \
{
        'ʔ': 4,
        'p': 6,
        't': 15,
        'k': 13,
        'r': 9,
        'l': 10,
        'n': 9,
        'y': 4,
        'w': 4,
        'G': 4,
}

vowels = \
{
        'a': 50,
        'i': 50,
        'u': 40,
}

prevowels = \
{
        'a': 5,
        'i': 3,
}

affixes = \
{
        'ʔ': 4,
        'p': 4,
        't': 15,
        'k': 12,
        'r': 12,
        'l': 10,
        'n': 10,
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
    if word[-1] not in 'aiuywr' and randrange(10) < 5: word += 'ʲ'
    if (randrange(10) < 8):
        word += select(affixes)
        if word[-1] not in 'aiuywr' and randrange(10) < 5: word += 'ʲ'
    print(word)
    exit(0)

def add_consonant():
    x = select(consonants)
    if x == 'y' or x == 'w':
        return x
    if (len(x) > 0 and randrange(10) < 5): x += 'ʲ'
    if x[0] == 'r':
        return x
    t = randrange(20);
    if (t < 3):
        x = x + 'ʔ'
    elif (t > 14):
        x = 'ʔ' + x
    return x

t = randrange(10)

if (t < 4):
    word += select(prevowels)
    word += add_consonant()

word += add_consonant()
word += select(vowels)
word += add_consonant()
if (randrange(10) < 4):
    word += add_consonant()

if (t == 4):
    word += select(vowels)
    word += add_consonant()
    if (randrange(10) < 4):
        word += add_consonant()

word = word.replace('ʔʔ', 'ʔ')

print(word)
