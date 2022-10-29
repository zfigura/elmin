# -*- coding: utf-8 -*-
vowels = u'aeiouāēīōūâêîôû'

def deriv(word, stages=False):
	if type(word) == str: word = list(unicode(word,'utf-8'))
	elif type(word) == unicode: word = list(word)
	#assimilate and IPA-ize geminated nasals
	for ph in range(1,len(word)-1):
		if word[ph] in 'mn' and word[ph-1] in 'mn':
			word[ph-1] += u'ː'
			word[ph] = 'x'
	while 'x' in word: word.remove('x')
	#velarize
	for ph in range(1,len(word)):
		if word[ph-1][0] == 'g':
			word[ph] = u'ŋ'+word[ph][1:]
			word[ph-1] = 'x'
	while 'x' in word: word.remove('x')
	if stages: print ''.join(word)
	#stress accent
	if u'́' in word: stress = word.index(u'́')-1
	else:
		stress = 1 #second letter must always be a vowel... sneaky rite?
		stone = 0
		for ph in range(1,len(word)):
			if word[ph][0] in u'eiou' and stone == 0: stress = ph
			if word[ph][0] in u'aāēīōū' and stone <= 1:
				stress = ph
				stone = max(stone,1)
			if word[ph][0] in u'âêîôû':
				stress = ph
				stone = max(stone,2)
	while u'́' in word: word.remove(u'́')
	vowel = True
	for ph in range(stress,0,-1):
		if word[ph][0] in vowels:
			if vowel: word[ph] += u'ˈ'
			vowel = not vowel
	if stages: print ''.join(word)
	#stop-ify
	word2 = []
	if word[0] == 'm': word2.append(u'b')
	elif word[0] == 'n': word2.append(u'd')
	else: word2.append(word[0])
	for ph in range(1,len(word)):
		if u'ˈ' in word[ph-1]:
			if u'ː' in word[ph] and word[ph][0] in u'mnŋ':
				word2.append(word[ph])
			elif word[ph] == u'm':
				word2.append(u'm')
				word2.append(u'b')
			elif word[ph] == u'n':
				word2.append(u'n')
				word2.append(u'd')
			elif word[ph] == u'ŋ':
				word2.append(u'ŋ')
				word2.append(u'g')
			else: word2.append(word[ph])
		else:
			if u'ː' in word[ph]:
				if word[ph][0] == u'm':
					word2.append(u'm')
					word2.append(u'b')
				elif word[ph][0] == u'n':
					word2.append(u'n')
					word2.append(u'd')
				elif word[ph][0] == u'ŋ':
					word2.append(u'ŋ')
					word2.append(u'g')
				else: word2.append(word[ph])
			elif word[ph][0] == u'm': word2.append(u'b')
			elif word[ph][0] == u'n': word2.append(u'd')
			elif word[ph][0] == u'ŋ': word2.append(u'g')
			else: word2.append(word[ph])
	word = word2
	del word2
	if stages: print ''.join(word)
	#high tone devoicing
	for ph in range(0,len(word)-1):
		if word[ph+1] in u'âêîôû':
			if word[ph] == 'b': word[ph] = 'f'
			elif word[ph] == 'd': word[ph] = 't'
			elif word[ph] == 'g': word[ph] = 'c'
	#low tone aspiration!
	for ph in range(0,len(word)-1):
		if word[ph][0] in 'eiou':
			word[ph+1] += u'ʰ'
	mutation = (word[-1][0] in 'eiou')
	if stages: print ''.join(word)+(u'ᴴ' if mutation else '')
	#remove tone and w > l, elide v and ə, ŋ > n
	for ph in range(0,len(word)):
		if word[ph][0] in u'āâ': word[ph] = 'a'+word[ph][1:]
		elif word[ph][0] in u'ēê': word[ph] = 'e'+word[ph][1:]
		elif word[ph][0] in u'īî': word[ph] = 'i'+word[ph][1:]
		elif word[ph][0] in u'ōô': word[ph] = 'o'+word[ph][1:]
		elif word[ph][0] in u'ūû': word[ph] = 'u'+word[ph][1:]
		elif word[ph][0] == u'w': word[ph] = 'l'+word[ph][1:]
		elif word[ph][0] in u'vβa': word[ph] = 'x'
		elif word[ph][0] == u'ŋ': word[ph] = 'n'+word[ph][1:]
	#ELIDE ALL THE THINGS
	for ph in range(0,len(word)-1):
		if word[ph][0] == 'd' and word[ph+1][0] in 'aei': word[ph] = 'x'
		elif word[ph][0] == 'b' and word[ph+1][0] in 'ou': word[ph] = 'x'
	while 'x' in word: word.remove('x')
	if stages: print ''.join(word)+(u'ᴴ' if mutation else '')
	if word[-1][0] in 'aeiou':
		if len(word) < 2: pass
		elif word[-2][0] in 'aeiou' or word[-3][0] in 'aeiou': word = word[:-1]
		elif u'ˈ' in word[-1]: word[-1] = word[-1].replace(u'ˈ',u'')
		else: word = word[:-2]
	else: word = word[:-1]
	return ''.join(word)+(u'ᴴ' if mutation else '')
