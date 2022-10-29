# -*- coding: utf-8 -*-

cons = u'ptckqbdgfvsʃzʒhlʎrwjmn'
obst = u'ptckqbdgfvsʃzʒhlʎrmn'
plos = u'ptckqbdg'
liquid = u'lʎrwjmn'
vowel = u'aeiouɑøyæəꜵ'

def deriv(word, stages=False):
	if type(word) == str: word = list(unicode(word,'utf-8'))
	elif type(word) == unicode: word = list(word)
	#VV > Vː
	for ph in range(0,len(word)-1):
		if word[ph] in vowel and word[ph+1] in vowel:
			word[ph] += u'ː'
			word[ph+1] = 'x'
	while 'x' in word: word.remove('x')
	#VjV > Vːː
	for ph in range(1,len(word)-1):
		if word[ph-1] in vowel and word[ph] in u'ːrj' and word[ph+1] in vowel:
			word[ph-1] += u'̂'
			word[ph] = 'x'
			word[ph+1] = word[ph-1]
	while 'x' in word: word.remove('x')
	#IPA-ize aspirates and long vowels
	for ph in range(0,len(word)-1):
		if word[ph] in 'ptkq' and word[ph+1] == u'ʰ':
			word[ph] += u'ʰ'
			word[ph+1] = 'x'
		elif word[ph] in vowel and word[ph+1] == u'ː':
			word[ph] += u'ː'
			word[ph+1] = 'x'
		elif word[ph][0] in vowel and word[ph+1] == u'ː':
			word[ph+1] = 'x'
	#Northern consonant shift
	for ph in range(0,len(word)-1):
		if word[ph+1][0] in vowel:
			if word[ph] == 't': word[ph] = u's'
			elif word[ph] == 'd': word[ph] = u'z'
		if word[ph] == 'D': word[ph] = u'd'
		elif word[ph] == 'T': word[ph] = u't'
	if word[-1] == 'D': word[-1] = u'd'
	elif word[-1] == 'T': word[-1] = u't'
	while 'x' in word: word.remove('x')
	#Voicing assimilation
	for ph in range(0,len(word)-1):
		if word[ph+1][0] in u'ptkqs':
			if word[ph][0] in u'pb': word[ph] = u'p'
			elif word[ph][0] in u'td': word[ph] = u't'
			elif word[ph][0] in u'kg': word[ph] = u'k'
			elif word[ph][0] == u'q': word[ph] = u'q'
		elif word[ph+1] in u'bdgz':
			if word[ph][0] in u'pb': word[ph] = u'b'
			elif word[ph][0] in u'td': word[ph] = u'd'
			elif word[ph][0] in u'kg': word[ph] = u'g'
			elif word[ph][0] == u'q': word[ph] = u'g'
	#Audex' law
	for ph in range(2,len(word)-1):
		if word[ph-2][0] in cons and word[ph-1] in liquid and word[ph][0] in vowel and (not stressed(word,ph)) and word[ph+1][0] in cons:
			word[ph-1],word[ph] = word[ph],word[ph-1]
	if stages: print u''.join(word)
	for ph in range(0,len(word)-1):
		#Palatalize
		if word[ph][0] in obst and word[ph+1] == 'j':
			if word[ph] in [u'tʰ',u'kʰ']: word[ph] = u'tɕʰ'
			elif word[ph] in 'tk': word[ph] = u'tɕ'
			elif word[ph] in 'dg': word[ph] = u'dʑ'
			elif word[ph] == u'qʰ': word[ph] = u'kχʰ'
			elif word[ph] == 'q': word[ph] = u'kχ'
			elif word[ph] == 's': word[ph] = u'ʃ'
			elif word[ph] == 'z': word[ph] = u'ʒ'
			elif word[ph] == 'l': word[ph] = u'ʎ'
			word[ph+1] == 'x'
		#Labialize
		elif word[ph][0] in obst and word[ph+1] == 'w':
			if word[ph][0] in 'tckqdg': word[ph] += u'ʷ'
			word[ph+1] == 'x'
		#/w/ > /v/
		if word[ph] == 'w' and word[ph-1][0] in vowel and word[ph+1][0] in vowel:
			word[ph] = u'v'
	if word[0] == 'w': word[0] == 'v'
	for ph in range(1,len(word)-1):
		#Break ī, ū
		if word[ph] == 'i' and word[ph+1] == 'j':
			word[ph] = u'iə'
			word[ph+1] = 'x'
		elif word[ph] == u'iː':
			word[ph] = u'iə'
		elif word[ph] == 'u' and word[ph+1] == 'w':
			word[ph] = u'uə'
			word[ph+1] = 'x'
		elif word[ph] == u'uː':
			word[ph] = u'uə'
		elif word[ph] == 'o' and word[ph+1] == 'j':
			word[ph] = u'øː'
			word[ph+1] = 'x'
		elif word[ph] == 'u' and word[ph+1] == 'j':
			word[ph] = u'yː'
			word[ph+1] = 'x'
		elif word[ph] == 'e' and word[ph+1] == 'w':
			word[ph] = u'ø'
		elif word[ph] == 'i' and word[ph+1] == 'w':
			word[ph] = u'y'
	while 'x' in word: word.remove('x')
	#Umlaut
	for ph in range(0,len(word)):
		if word[ph][0] in u'ɑou' and nextv(word,ph) != 'x' and word[nextv(word,ph)][0] == 'i' and not (u'ə' in word[ph]):
			word[ph] = u'aøy'[u'ɑou'.index(word[ph][0])]+word[ph][1:]
	#Diphthong resolution
	for ph in range(0,len(word)-1):
		if word[ph+1] == 'j' and word[ph] in u'ɑae':
			word[ph] = u'aei'[u'ɑae'.index(word[ph])]+u'ː'
			word[ph+1] = 'x'
		elif word[ph+1] == 'w' and word[ph] in u'aɑo':
			word[ph] = u'ɑou'[u'aɑo'.index(word[ph])]+u'ː'
			word[ph+1] = 'x'
		elif word[ph+1][0] == 'r' and word[ph] in u'ieaɑou':
			word[ph] = u'eaɑɑɑo'[u'ieaɑou'.index(word[ph])]+u'ː'
			word[ph+1] = 'x'
	while 'x' in word: word.remove('x')
	#Danthrôs' law
	for ph in range(1,len(word)):
		if (ph == len(word)-1 or word[ph+1][0] in cons) and word[ph-1][0] in vowel:
			if ph < len(word)-1 and word[ph+1] in u'lr': continue
			if ph < len(word)-1 and word[ph+1][0] in u'tdsz' and word[ph] in u'pbkgq': continue
			if u'ʰ' in word[ph]: word[ph] = word[ph].replace(u'ʰ',u'')
			elif word[ph] == u'p': word[ph] = u'f'
			elif word[ph] == u'b': word[ph] = u'v'
			elif word[ph] == u't': word[ph] = u's'
			elif word[ph] == u'd': word[ph] = u'z'
			elif word[ph] == u'k': word[ph] = u'ʃ'
			elif word[ph] == u'g': word[ph] = u'ʒ'
			elif word[ph] == u'q': word[ph] = u'h'
	if stages: print ''.join(word)
	for ph in range(0,len(word)-1):
		if u'ʷ' in word[ph]:
			if word[ph+1][0] in u'ouøy':
				word[ph] = word[ph].replace(u'ʷ',u'')
			if ph > 0:
				if word[ph-1][0] in u'ouøy':
					word[ph] = word[ph].replace(u'ʷ',u'')
	for ph in range(0,len(word)):
		if u'kχ' in word[ph]: word[ph] = u'h'
		elif u'ʃ' in word[ph]: word[ph] = u'h'
		elif u'ʒ' in word[ph]: word[ph] = u'x'
		elif u'tɕ' in word[ph]: word[ph] = u'ts'
		elif u'dʑ' in word[ph]: word[ph] = u'dz'
	while 'x' in word: word.remove('x')
	#Dipth. height harmony
	for ph in range(0,len(word)):
		if u'ə' in word[ph]:
			if word[ph] == u'iə': word[ph] = u'eə'
			elif word[ph] == u'uə': word[ph] = u'oə'
	#nasalize when closed
	for ph in range(0,len(word)-2): #don't nasalize -Vn
		if closed(word,ph) and word[ph] in vowel and word[ph+1][0] in 'mn':
			word[ph] += u'̃'
			word[ph+1] = 'x'
	while 'x' in word: word.remove('x')
	#Cʷ resolution
	for ph in range(0,len(word)-1):
		if u'ʷ' in word[ph]:
			if word[ph+1][0] in u'eiøy':
				if word[ph][0] in 'kq': word[ph] = u't'+word[ph][1:]
				elif word[ph][0] == 'g': word[ph] = u'd'+word[ph][1:]
				word[ph] = word[ph].replace(u'ʷ',u'')
			else:
				if word[ph][0] in 'tkq': word[ph] = u'p'+word[ph][1:]
				elif word[ph][0] == 'dg': word[ph] = u'b'+word[ph][1:]
				word[ph] = word[ph].replace(u'ʷ',u'')
	word[-1] = word[-1].replace(u'ʷ',u'')
	#/l/ diverges
	for ph in range(1,len(word)):
		if word[ph][0] == 'l':
			if ph < len(word)-1 and word[ph+1][0] in vowel: continue
			if word[ph-1][0] in u'aeiøy': word[ph] = u'ʎ'
			elif word[ph-1][0] in u'ɑou': word[ph] = u'ɫ'
##	#/h/ > /f/
##	for ph in range(1,len(word)-1):
##		if word[ph][0] == 'h' and (word[ph-1][0] in cons or word[ph+1][0] in cons):
##			word[ph] = u'f'
	if stages: print ''.join(word)
	#chainshift short vowels
	for ph in range(0,len(word)):
		if word[ph] == u'i': word[ph] = u'e'
		elif word[ph] == u'e': word[ph] = u'a'
		elif word[ph] == u'a': word[ph] = u'ɑ'
		elif word[ph] == u'ɑ': word[ph] = u'o'
		elif word[ph] == u'o': word[ph] = u'u'
		elif word[ph] == u'eə': word[ph] = u'aə'
		elif word[ph] == u'oə': word[ph] = u'uə'
	#Palatalize k > s
	for ph in range(0,len(word)-1):
		if word[ph] == 'k' and word[ph+1][0] in u'eiøy':
			word[ph] = 's'
	#Reduce unstr. /aə uə/
	for ph in range(0,len(word)):
		if not stressed(word,ph):
			if word[ph] == u'aə': word[ph] = u'a'
			elif word[ph] == u'uə': word[ph] = u'u'
	#Reduce unstr. /i u y/
	for ph in range(0,len(word)):
		if word[ph] in u'iuy' and not stressed(word,ph):
			if word[ph] == 'i': word[ph] = u'e'
			elif word[ph] == 'u': word[ph] = u'o'
			elif word[ph] == 'y': word[ph] = u'ø'
	#shorten remaining geminates
	for ph in range(1,len(word)):
		if word[ph-1] == word[ph][0]: word[ph-1] = 'x'
	while 'x' in word: word.remove('x')
	#Rhotacise
	for ph in range(1,len(word)-1):
		if word[ph-1][0] in vowel+u'vʎɫ' and word[ph+1][0] in vowel+u'vʎɫ' and word[ph] == u'z':
			word[ph] = u'r'
	#Anglo-Frisian brightening
	for ph in range(0,len(word)-1):
		if word[ph] == 'a' and nextv(word,ph) != 'x' and word[nextv(word,ph)][0] in u'eiøy':
			word[ph] = u'æ'
	#uvu > vel > pal
	for ph in range(0,len(word)):
		if word[ph][0] == 'k': word[ph] = u'c'+word[ph][1:]
		elif word[ph][0] == 'q': word[ph] = u'k'+word[ph][1:]
	if stages: print ''.join(word)
	#short ɑ > ə
	for ph in range(0,len(word)):
		if word[ph] in u'ɑ̃': word[ph] = u'ə'+word[ph][1:]
	#long ɑ > ao
	for ph in range(0,len(word)):
		if word[ph][0] == u'ɑ': word[ph] = u'ao'
	#Chainshift vowels
	for ph in range(0,len(word)):
		if word[ph] == u'æ': word[ph] = u'e'
		elif word[ph] == u'e' and stressed(word,ph): word[ph] = u'i'
	#Remove /w j z/
	for ph in range(0,len(word)):
		if word[ph][0] in 'wjz': word[ph] = 'x'
	while 'x' in word: word.remove('x')
	#Defront vowels
	for ph in range(0,len(word)):
		if word[ph][0] == u'ø': word[ph] = u'o'+word[ph][1:]
		if word[ph][0] == u'y': word[ph] = u'u'+word[ph][1:]
	#final stops
	if word[-1] in u'pbckg': word.append(u's')
	for ph in range(0,len(word)):
		if word[ph] == u'ʎ': word[ph] = u'i'
		elif word[ph] == u'ɫ': word[ph] = u'u'
		if u'̃' in word[ph]: word[ph] = word[ph].replace(u'̃',u'')
		if word[ph] == u'ə': word[ph] = u'e'
		if u'ə' in word[ph]: word[ph] = word[ph][0]+u'e'
	return ''.join(word).encode('utf-8')

def nextv(word,ph):
	'''find the next vowel in the word'''
	if ph == len(word)-1: return 'x'
	for i in range(ph+1,len(word)):
		if word[i][0] in vowel: return i
	return 'x'

def stressed(word,ph):
	'''returns True if the vowel is stressed'''
	q = nextv(word,0)
	if q == len(word)-1: return True
	if ph == q: return True
	return False

def closed(word,ph):
	'''A syllable is closed if the vowel is followed by C^ or CC but not RS.'''
	if not (word[ph] in vowel): return False
	if ph == len(word)-1: return False
	elif ph == len(word)-2: return not (word[ph+1][0] in vowel)
	elif ph == len(word)-3: return not (word[ph+2][0] in vowel)
	else:
		if word[ph+1][0] in vowel: return False
		elif word[ph+2][0] in vowel: return False
		elif word[ph+3][0] in vowel and word[ph+1][0] in liquid and word[ph+2][0] in plos: return False
		return True
