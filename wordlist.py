# wordlist.py

import os
import re
import operator
import utils
import config

class WordList:

	def __init__(self, dir:str, filename:str):
		# Einlesen
		textfile = open(os.path.join(os.getcwd(), dir, filename), 'r')
		self.filetext = textfile.read().upper()
		textfile.close()
		# Buchstabenhäufigkeit
		self.bcount = {
			'A':0., 'B':0., 'C':0., 'D':0., 'E':0., 'F':0., 'G':0., 'H':0., 'I':0.,
			'J':0., 'K':0., 'L':0., 'M':0., 'N':0., 'O':0., 'P':0., 'Q':0., 'R':0., 
			'S':0., 'T':0., 'U':0., 'V':0., 'W':0., 'X':0., 'Y':0., 'Z':0.
			}
		btotal = 0.
		for c in [*(self.filetext)]:
			if c.isalpha():
				btotal = btotal + 1.
				self.bcount[c] = self.bcount[c] + 1.
		for k in self.bcount.keys():
			self.bcount[k] = self.bcount[k] / btotal * 100.

	def dosearch(self, knvletters:str, cletter:list, fletters:list, fletters_unique:list) -> str:
		# Reg. Ausdruck erzeugen
		nots = ''.join(['^' + c for c in [*knvletters]])
		regex = []
		for i in range(5):
			regex.append(cletter[i])
			if len(regex[i]) > 1:
				regex[i] = regex[i][0]
			if regex[i] == '':
				x = nots
				if len(fletters[i]) > 0:
					x = x + ''.join(['^' + c for c in [*(fletters[i])]])
				regex[i] = '[' + x + ']'
				if regex[i] == '[]':
					regex[i] = '.'
		regex2 = ''
		for c in fletters_unique:
			regex2 = regex2 + '(?=.*' + c + '.*)'
		regex2 = '^' + regex2 + ''.join(regex) + '$'
		if config.DEBUG:
			print('RE = ' + regex2)
		# Suche
		resultarr = re.findall(regex2, self.filetext, re.IGNORECASE + re.MULTILINE)
		# Ergebnis sortieren 
		results = {}
		for r in resultarr:
			lettercount = len(utils.unique_str(r)) # 5: all different, 6+: 1,2,.. not different
			results[r] = (self.bcount[r[0]] + self.bcount[r[1]] + self.bcount[r[2]] + 
				self.bcount[r[3]] + self.bcount[r[4]]) / (10. - lettercount)
		sortedresults = dict(sorted(results.items(), key=operator.itemgetter(1), reverse=True))
		return " ".join(list(sortedresults.keys()))
