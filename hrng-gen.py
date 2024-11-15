#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randrange
import re

initials = \
{
        't': 130,
        'r': 120,
        'q': 100,
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
        'ə': 30,
        'e': 30,
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
word = word.replace('ə','')
word = re.sub('[ptkq]l','tɬ',word)
word = re.sub('r([tkqnŋl])',r'\1.',word)
word = re.sub('([tkqnŋl])r',r'\1.',word)
word = re.sub('([ui])([tkqnŋl])',r'\1\2.',word)
word = re.sub('^[aeiou]','',word)
word = word.replace('p','')
word = re.sub('(^|[aeiou])re',r'\1ne',word)
word = re.sub('(^|[aeiou])r($|[iaou])',r'\1n.\2',word)
word = re.sub('l($|[tkqmnŋ])',r'n\1',word)
word = word.replace('r','')

# replace first /e/ with /a/
for i in range(len(word)):
        if word[i] == 'e':
                word = word[:i] + 'a' + word[i+1:]
        if word[i] in 'aeiou':
                break

word = re.sub('i','e',word)
word = re.sub('u','o',word)

print(word)
