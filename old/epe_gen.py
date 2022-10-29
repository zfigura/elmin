# -*- coding: utf-8 -*-
import random

def word():
	r = random.random()
	q = u''
	for i in range(int(3.1*2**r)): q += syl()
	return q

def affix():
        q = syl()
        if random.random() < 0.3: q += syl()
        return q

def suffix():
	r = random.random()
	q = u''
	for i in range(int(2.1*2**r)): q += syl()
	return q

def syl():
	if random.random() < 0.5: return unicode(icons()+vowel()+cons(),'utf-8')
	return unicode(icons()+vowel(),'utf-8')

def icons(): #initial consonant (excludes ⟨gm gn⟩)
	r = random.random()
	if (r < 0.35): return 'm'
	elif (r < 0.7): return 'n'
	elif (r < 0.8): return 'w'
	elif (r < 0.88): return 'r'
	elif (r < 0.94): return 'j'
	return 'β'

def cons():
	r = random.random()
	if (r < 0.3): return 'm'
	elif (r < 0.6): return 'n'
	elif (r < 0.7): return 'gm'
	elif (r < 0.8): return 'gn'
	elif (r < 0.86): return 'w'
	elif (r < 0.94): return 'r'
	elif (r < 0.97): return 'j'
	return 'β'

def vowel():
	r = random.random()
	if (r < 0.05): return 'a'
	elif (r < 0.3): return tone('u','ū','û')
	elif (r < 0.55): return tone('o','ō','ô')
	elif (r < 0.75): return tone('ā','ā','â')
	elif (r < 0.9): return tone('e','ē','ê')
	return tone('i','ī','î')

def tone(l,m,h):
	r = random.random()
	if (r < 0.4): return l
	if (r < 0.75): return m
	return h
