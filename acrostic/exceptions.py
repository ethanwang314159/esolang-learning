import sys

class AmbiguousStartPosition(Exception):
	def __init__(self, positions):
		positions_str = ", ".join("({}, {})".format(*p) for p in positions)
		super().__init__("Ambiguous starting position: {}".format(positions_str))

class InvalidPosition(Exception):
	def __init__(self, pos):
		super().__init__("Invalid position ({}, {})".format(*pos))

class MathError(Exception):
	def __init__(self, s):
		super().__init__("Math error: {}".format(s))

class NoStartPosition(Exception):
	def __init__(self):
		super().__init__("No starting position")

class NoSuchWord(Exception):
	def __init__(self, w):
		super().__init__("No such word '{}'".format(w))

class StackUnderflow(Exception):
	def __init__(self):
		super().__init__("Stack underflow")

def exit_with_error(s):
	sys.stderr.write(str(s))
	sys.exit(1)