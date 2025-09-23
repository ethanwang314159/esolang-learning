from types import SimpleNamespace

from exceptions import *
from standard_dictionary import *
import word_parser

class Dictionary:
	def __init__(self, words):
		self.word_map = {}
		
		for e in words.entries:
			for word in e.forward.words:
				self.word_map[word] = SimpleNamespace(**{
					"forward": e.forward,
					"backward": e.backward,
					"forward_branch": e.forward_branch,
					"backward_branch": e.backward_branch})
			for word in e.backward.words:
				self.word_map[word] = SimpleNamespace(**{
					"forward": e.backward,
					"backward": e.forward,
					"forward_branch": e.backward_branch,
					"backward_branch": e.forward_branch})
		
		self.starting_word = words.starting_word
	
	def find_word(self, word):
		try:
			return self.word_map[word]
		except KeyError:
			raise NoSuchWord(word) from None
	
	def synonyms_of(self, word):
		return self.find_word(word).forward.words
	
	def antonyms_of(self, word):
		return self.find_word(word).backward.words
	
	def execute_forward(self, word, state):
		self.find_word(word).forward.func(state)
	
	def execute_backward(self, word, state):
		self.find_word(word).backward.func(state)
	
	def should_acknowledge(self, word, state):
		if word is None:
			return False
		
		rel_pos = word_parser.position_in_word(word, state.pointer)
		forward = 2 * rel_pos < len(word.text)
		entry = self.find_word(word.text)
		
		return entry.forward_branch(state) if forward else entry.backward_branch(state)