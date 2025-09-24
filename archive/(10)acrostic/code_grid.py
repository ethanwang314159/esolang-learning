import string
import numpy as np

import word_parser

class Grid:
	def __init__(self, text):
		self.populate(text)
	
	def populate(self, text):
		lines = text.splitlines()
		self.w = max(len(line) for line in lines)
		self.h = len(lines)
		
		self.grid = np.full((self.w, self.h), None)
		
		for y, line in enumerate(text.splitlines()):
			for x, c in enumerate(line):
				if c in string.ascii_letters:
					self.grid[x,y] = c.upper()
	
	def validate(self, dict):
		for word in word_parser.find_all_words(self):
			dict.find_word(word.text)
	
	def is_in_bounds(self, pos):
		x, y = pos
		return x >= 0 and x < self.w and y >= 0 and y < self.h