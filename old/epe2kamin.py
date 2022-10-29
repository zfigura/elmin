# -*- coding: utf-8 -*-
vowels = u'aeiouāēīōūâêîôû'
def deriv(word,stages=False):
	if type(word) == str: word = list(unicode(word,'utf-8'))
	elif type(word) == unicode: word = list(word)
	#IPA-ize geminated consonants
	for ph in range(1,len(word)-1):
		if word[ph] in 'mn' and word[ph-1] == word[ph]:
			word[ph-1] += u'ː'
			word[ph] = 'x'
	while 'x' in word: word.remove('x')
	#Shortening
	if word[0] in 'mn' and word[1] in 'eiou': word[0] = 'x'
	for ph in range(1,len(word)-1):
		if word[ph-1] in vowels and \
		   word[ph-1] != 'a' and \
		   word[ph+1] in vowels and \
		   word[ph][0] in 'mn':
			if word[ph][1:] == u'ː': word[ph] = word[ph][0]
			else: word[ph] = 'x'
	if word[-1] in 'mn' and word[-2] in 'eiou': word[-1] = 'x'
	while 'x' in word: word.remove('x')
	if stages: print ''.join(word)
	#Clusters simplify
	for ph in range(1,len(word)):
		if word[ph] in vowels and word[ph-1] in vowels:
			word[ph-1] += u'ː'
			word[ph] = 'x'
		elif word[ph] in vowels and word[ph-1] == 'x': word[ph] = 'x'
	while 'x' in word: word.remove('x')
	if stages: print ''.join(word)
	#/w/,/ɰ/ > /h/
	if word[0] == 'w':
		word[0] = 'x'
		word[1] += u'̃'
	for ph in range(1,len(word)-1):
		if word[ph] in 'wg':
			if not (word[ph-1][0] in vowels): word[ph-1] += u'̥'
			elif not (word[ph+1][0] in vowels): word[ph+1] += u'̥'
			else: word[ph+1] += u'̃'
			word[ph] = 'x'
	for ph in range(1,len(word)-1):
		if u'̥̥' in word[ph]: word[ph] = word[ph][:-1] #remove double devoicing
		if u'ː̥' in word[ph]: word[ph] = word[ph][0]+u'̥ː' #metathesize diacritics for æsthetics' sake
		if u'̥' in word[ph]:
			if word[ph-1] in u'mnβrj': word[ph-1] += u'̥'
			if word[ph+1] in u'mnβrj': word[ph+1] += u'̥'
	if word[-1] == 'w': word[-1] = 'x'
	while 'x' in word: word.remove('x')
	if stages: print ''.join(word)
	#n > ɲ
	if word[0][0] == 'n' and not (word[1][0] in u'eiēīêî'): word[0] = u'ɲ'
	for ph in range(1,len(word)-1):
		if word[ph][0] == 'n' and \
		   not (word[ph-1][0] in u'eiēīêîm') and \
		   not (word[ph+1][0] in u'eiēīêîm'): word[ph] = u'ɲ'+word[ph][1:]
	if word[-1][0] == 'n' and not (word[-2][0] in u'eiēīêî'): word[-1] = u'ɲ'+word[-1][1:]
	#mn > n
	for ph in range(1,len(word)-1):
		if word[ph][0] == 'm' and (word[ph-1][0] == 'n' or word[ph+1][0] == 'n'): word[ph] = 'x'
	while 'x' in word: word.remove('x')
	if stages: print ''.join(word)
	#nasals and approximants assimilate to approximants
	for ph in range(1,len(word)-1):
		if word[ph][0] == u'β':
			if word[ph-1][0] in u'mnɲ':
				word[ph-1] = u'm'+word[ph-1][1:]
				word[ph] = 'x'
			elif word[ph+1][0] in u'mnɲ':
				word[ph+1] = u'm'+word[ph+1][1:]
				word[ph] = 'x'
			elif word[ph-1][0] in u'βrj':
				word[ph-1] += u'ː'
				word[ph] = 'x'
		elif word[ph][0] == u'r':
			if word[ph-1][0] in u'mnɲ':
				word[ph-1] = u'n'+word[ph-1][1:]
				word[ph] = 'x'
			elif word[ph+1][0] in u'mnɲ':
				word[ph+1] = u'n'+word[ph+1][1:]
				word[ph] = 'x'
			elif word[ph-1][0] in u'βrj':
				word[ph-1] += u'ː'
				word[ph] = 'x'
		elif word[ph][0] == u'j':
			if word[ph-1][0] in u'mnɲ':
				word[ph-1] = u'ɲ'+word[ph-1][1:]
				word[ph] = 'x'
			elif word[ph+1][0] in u'mnɲ':
				word[ph+1] = u'ɲ'+word[ph+1][1:]
				word[ph] = 'x'
			elif word[ph-1][0] in u'βrj':
				word[ph-1] += u'ː'
				word[ph] = 'x'
	while 'x' in word: word.remove('x')
	if stages: print ''.join(word)
	#stops and fricatives now form
	for ph in range(len(word)):
		if word[ph][0] in vowels: continue
		gem = False
		if u'ː' in word[ph]:
			gem = True
			word[ph] = word[ph].replace(u'ː',u'')
		word[ph] = {u'm':u'b',u'm̥':u'p',
			    u'n':u'd',u'n̥':u't',
			    u'ɲ':u'ɟ',u'ɲ̥':u'c',
			    u'β':u'β',u'β̥':u'ɸ',
			    u'r':u'z',u'r̥':u's',
			    u'j':u'ʝ',u'j̥':u'ç'}[word[ph]]
		if gem: word[ph] += u'ː'
	if stages: print ''.join(word)
	#initial/final lenition
	if not (word[0][0] in vowels):
		word[0] = {u'b':u'p',u'p':u'ɸ',
			   u'd':u't',u't':u's',
			   u'ɟ':u'c',u'c':u'ç',
			   u'β':u'ɸ',u'z':u's',u'ʝ':u'ç'}[word[0]]
	if not (word[-1][0] in vowels):
		word[-1] = {u'b':u'p',u'p':u'ɸ',
			   u'd':u't',u't':u's',
			   u'ɟ':u'c',u'c':u'ç',
			   u'β':u'ɸ',u'z':u's',u'ʝ':u'ç'}[word[-1]]
	if stages: print ''.join(word)
	#renasalization
	for ph in range(len(word)):
		if u'̃' in word[ph]:
                        if u'ː' in word[ph]: word[ph] = word[ph].replace(u'ː','')
                        else: word[ph] = u'n'
        if stages: print ''.join(word)
	#low-tone deletion
	for ph in range(len(word)):
		if word[ph][0] in 'eiou' and u'ː' in word[ph]: word[ph] = word[ph][0]
		elif word[ph] in 'eiou': word[ph] = 'x'
	while 'x' in word: word.remove('x')
	if stages: print ''.join(word)
	#high gemination
	for ph in range(1,len(word)-1):
		if word[ph-1][0] in u'âêîôû' and not (u'ː' in word[ph]):
			word[ph] += u'ː'
	#tone distinction lost (and IPA-ize the vowels)
	for ph in range(len(word)):
		if word[ph][0] in vowels:
			word[ph] = {u'a':u'ə',u'i':u'i',u'e':u'e',u'o':u'o',u'u':u'u',
				    u'ā':u'ɑ',u'ī':u'i',u'ē':u'e',u'ō':u'o',u'ū':u'u',
				    u'â':u'ɑ',u'î':u'i',u'ê':u'e',u'ô':u'o',u'û':u'u'}[word[ph][0]]+word[ph][1:]
	return ''.join(word).encode('utf-8')

def mderiv(stages=False):
	'''Derives multiple roots at a time.'''
	roots = [0]
	while roots[-1] != '': roots.append(raw_input())
	for i in roots[1:-1]: print i+'\t'+deriv(i)
