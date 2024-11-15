# -*- coding: utf-8 -*-
import random

def word():
	q = init()
	for i in range(4):
		q += vowel() + mid()
	return q+vowel()+coda()

def init():
	CF = {'m':110,
	      'n':85,
	      'l':69,
	      'r':51,
	      't':47,
	      'b':36,
	      'd':29,
	      'ŋ':22,
	      'nt':17,
	      'mb':17,
	      '':15,
	      'c':11,
	      'nd':10,
	      'g':9,
	      'ng':5,
	      'nc':3,
	      'th':7,
	      'nth':2,
	      'ch':2,
	      'nch':1}
	r = random.random()*sum(CF.values())
	i = 0
	for ph in CF:
		i += CF[ph]
		if r <= i: return ph

def vowel():
	CF = {'a':200,
	      'e':100,
	      'i':75,
	      'u':55,
	      'ea':52,
	      'eo':40,
	      'o':38,
	      'y':32,
	      'ei':10,
	      'ui':6,
	      'ai':4,
	      'oi':2,
	      'ou':3,
	      'eu':2,
	      'au':1,
	      'ie':10,
	      'ia':6,
	      'iu':6,
	      'io':2}
	r = random.random()*sum(CF.values())
	i = 0
	for ph in CF:
		i += CF[ph]
		if r <= i: return ph

def mid():
	CF = {'nn':160,
	      'mm':120,
	      'll':80,
	      'rr':60,
              'ŋŋ':20,
	      'gm':8,
	      'gn':6,
	      'nd':100,
	      'mb':80,
	      'ng':30,
	      'm':20,
	      'n':16,
	      'l':10,
	      'r':6,
              'ŋ':2,
	      '̈':2}
	r = random.random()*sum(CF.values())
	i = 0
	for ph in CF:
		i += CF[ph]
		if r <= i: return ph

def coda():
	CF = {#'':100,
	      'n':80,
	      'm':50,
	      'ng':20,
	      'r':40,
	      'l':20,
	      'gm':25,
	      'gn':20}
	r = random.random()*sum(CF.values())
	i = 0
	for ph in CF:
		i += CF[ph]
		if r <= i: return ph
