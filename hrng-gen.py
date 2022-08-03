#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randrange
import re

initials = \
{
        't': 200,
        'r': 180,
        'q': 130,
        'n': 90,
        'y': 90,
        'k': 80,
        'w': 80,
        'l': 80,
        'm': 70,
        'p': 60,
        '': 50,
        'ŋ': 45,
}

medials = \
{
        'a': 50,
        'i': 50,
        'u': 35,
        'o': 25,
        'e': 15,
}

word = ''

def select(l):
        a = randrange(sum(l.values()))
        for k in l.keys():
                if a < l[k]:
                        return k
                a -= l[k]

for i in range(randrange(2, 4)):
        word += select(initials) + select(medials)

print(word)
word = word.replace('o','')
word = re.sub('[ptkq]l','tɬ',word)
word = word.replace('p','')
word = re.sub('r([tkqnŋl])',r'R\1',word)
word = re.sub('([tkqnŋl])r',r'R\1',word)
word = re.sub('([ui])([tkqnŋl])',r'\1R\2',word)
word = re.sub('([tkqnŋl])([ui])',r'R\1\2',word)
word = re.sub('(^|[aeiou])re',r'\1ne',word)
word = re.sub('(^|[aeiou])r($|[iaou])',r'\1Rn\2',word)
word = re.sub('l($|[tkqmnŋ])',r'n\1',word)

# replace first /e/ with /a/
for i in range(len(word)):
        if word[i] == 'e':
                word = word[:i] + 'a' + word[i+1:]
        if word[i] in 'aeiou':
                break

word = re.sub('i','e',word)
word = re.sub('u','o',word)

print(word)
