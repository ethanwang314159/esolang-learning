from code_grid import *
from dictionary import *
from evaluator import *
from exceptions import *
from standard_dictionary import *

if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser()
	parser.add_argument("filename",
		help = "program file",
		metavar = "<filename>")
	
	args = parser.parse_args()
	
	try:
		file_text = open(args.filename, "r").read()
	except FileNotFoundError:
		exit_with_error("File {} not found.".format(args.filename))
	except IOError:
		exit_with_error("Unexpected IO error.")
	
	dict = Dictionary(Words)
	grid = Grid(file_text)
	
	ev = Evaluator(grid, dict)
	
	try:
		ev.execute_code()
	except Exception as e:
		exit_with_error(str(e))