from exceptions import *
import word_parser

class Evaluator:
	def __init__(self, grid, dict):
		self.grid = grid
		self.dict = dict
		
		self.ascii = False
		self.terminated = False
		self.stack = []
		self.storage = []
		self.pointer = (0, 0)
		self.across = True
		self.forward = True
	
	def at_invalid_pos(self):
		if not self.grid.is_in_bounds(self.pointer):
			return True
		if self.grid.grid[self.pointer] is None:
			return True
		return False
	
	def execute_one_step(self):
		if self.at_invalid_pos():
			raise InvalidPosition(self.pointer) from None
		
		dir = not self.across
		word = word_parser.word_at(self.grid, dir, self.pointer)
		
		if self.dict.should_acknowledge(word, self):
			rel_pos = word_parser.position_in_word(word, self.pointer)
			if 2 * rel_pos < len(word.text):
				self.pointer = word.end_pos
				self.across = dir
				self.forward = True
				self.dict.execute_forward(word.text, self)
			else:
				self.pointer = word.start_pos
				self.across = dir
				self.forward = False
				self.dict.execute_backward(word.text, self)
		else:
			self.pointer = word_parser.move_in_dir(self.across, -1 if self.forward else 1, self.pointer)
	
	def execute_until_done(self):
		while not self.terminated:
			self.execute_one_step()
	
	def starting_state(self):
		self.grid.validate(self.dict)
		
		starting_words = self.dict.synonyms_of(self.dict.starting_word)
		ending_words = self.dict.antonyms_of(self.dict.starting_word)
		matches = word_parser.find_word(self.grid, starting_words + ending_words)
		
		if len(matches) == 1:
			word = matches[0]
			if word.text in starting_words:
				self.pointer = word.end_pos
				self.ascii = False
				self.terminated = False
				self.across = word_parser.direction_of(word)
				self.forward = True
				self.stack = []
				self.storage = []
			elif word.text in ending_words:
				self.pointer = word.start_pos
				self.ascii = False
				self.terminated = False
				self.across = word_parser.direction_of(word)
				self.forward = False
				self.stack = []
				self.storage = []
			else:
				raise NoStartPosition from None
		elif len(matches) == 0:
			raise NoStartPosition from None
		else:
			start_or_end = lambda w: w.start_pos if w.text in starting_words else w.end_pos
			raise AmbiguousStartPosition([start_or_end(m) for m in matches]) from None
	
	def execute_code(self):
		self.starting_state()
		self.execute_until_done()