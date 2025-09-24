#!/usr/bin/python

# An implementation of 2DFuck in Python 2
# Tested with Python 2.6.5 and 2.7.13

import sys, getopt

inf = float('inf')

def usage():
	print >> sys.stderr, '''\
Synopsis: %s [-ldh] [<file> | -e <expr>]

Options:
	-d
		Enable debugging information
	-l
		For '?' command: output 1 as '#' and 0 as ' '
	-e <expr>
		Run <expr>
	-h
		Show this help and exit''' % sys.argv[0]
	sys.exit(0)

def getchar():
	ch = sys.stdin.read(1)
	if ch: return ord(ch)
	return 0 # EOF

def putchar(x):
	debug('Printing: chr(%d)', x)
	sys.stdout.write(chr(x))
	sys.stdout.flush()

def error(msg):
	print >> sys.stderr, msg, 'at line', line
	sys.exit(3)

def debug(*args):
	global debugstr
	if debugging: put_stderr(*args)

def put_stderr(msg, *args):
	global debugstr
	debugstr += ('\n  '+msg) % args

def flush_debug(msg, *args):
	global debugstr
	if debugging:
		debugstr = '%s (line %d)%s' % ((msg % args), line, debugstr)
	debugstr = debugstr.strip("\n")
	if debugstr:
		print >> sys.stderr, debugstr
		debugstr = ""

def bit_length(n):
    bits = 0
    while n >> bits: bits += 1
    return bits

def lowest_set(n):
	if not n: return inf
	low = 0
	while not n >> low & 1: low += 1
	return low

try: opts, args = getopt.getopt(sys.argv[1:], 'ldhe:')
except getopt.GetoptError as err:
	usage()

code = None
debugging = False
chars = '01'

for opt, value in opts:
	if opt == '-d': debugging = not debugging
	elif opt == '-h': usage()
	elif opt == '-l': chars = ' #'
	elif opt == '-e':
		if code:
			print >> sys.stderr, 'Multiple expression options!'
			sys.exit(1)
		code = value

if code is None:
	if args and args[0] != '-':
		try:
			with open(args[0]) as f: code = f.read()
		except IOError as err:
			print >> sys.stderr, 'Error:', err.strerror
			sys.exit(2)
	else: code = sys.stdin.read()

if code[:2] == '#!':
	code = code.partition('\n')[2]
	line = 2
else: line = 1

field = [0]
xoff = 0
yoff = 0

x = 0
y = 0
acc = 0

in_char = 0
in_bit = 0

out_char = 0
out_bit = 8

debugstr = ""
brackets = []
i = 0

try:
	while i < len(code):
		char = code[i]
		i += 1
		oldacc = acc
		if char == '<':
			if x: x -= 1
			else:
				xoff += 1
				field = [ v << 1 for v in field ]
		elif char == '>':
			x += 1
		elif char == '^':
			if y: y -= 1
			else:
				yoff += 1
				field.insert(0, 0)
		elif char == 'v':
			y += 1
			if y >= len(field): field.append(0)
		elif char == '!':
			acc = not acc
		elif char == 'r':
			acc = field[y] >> x & 1
		elif char == 'x':
			# optimisation: don't index etc. if we won't change it
			if acc: field[y] ^= 2 ** x
		elif char == ',':
			if not in_bit:
				in_char = getchar()
				in_bit = 8
			in_bit -= 1
			acc = in_char >> in_bit & 1
		elif char == '.':
			out_char = out_char << 1 | acc
			debug('Character: %d', out_char)
			out_bit -= 1
			if not out_bit:
				putchar(out_char)
				out_bit = 8
				out_char = 0
		elif char == '[':
			if not acc:
				bracks = 1
				while bracks and i < len(code):
					char = code[i]
					i += 1
					if char == '[': bracks += 1
					elif char == ']': bracks -= 1
					elif char == '\n': line += 1
				if bracks:
					error("Missing ']'; '['")
					break
				debug('Skipping forward to line %d', line)
			else: brackets.append((i, line))
		elif char == ']':
			if not brackets: error("Unmatched ']'")
			if acc:
				i, line = brackets[-1]
				debug('Skipping back to line %d', line)
			else: brackets.pop()
		elif char == 'l':
			field.extend((0, 0))
			field.insert(0, 0)
			above = 0
			value = 0
			width = 0
			for _y, below in enumerate(field[1:]):
				below <<= 1
				new_above = value
				new_value = below
				width = max(width, bit_length(below)+1)
				abv_left = 0
				abv_here = above & 1
				blw_left = 0
				blw_here = below & 1
				left = 0
				cell = value & 1
				_x = 0
				field[_y] = 0
				while _x < width:
					_x += 1
					abv_right = above >> _x & 1
					blw_right = below >> _x & 1
					right = value >> _x & 1
					neighbors = \
					  abv_left + abv_here + abv_right + \
					    left        +         right   + \
					  blw_left + blw_here + blw_right
					if (cell and neighbors == 2) or neighbors == 3:
						field[_y] |= 1 << _x
					abv_left = abv_here
					abv_here = abv_right
					left = cell
					cell = right
					blw_left = blw_here
					blw_here = blw_right
				above = new_above
				value = new_value
			field.pop()
			x += 1
			y += 1
		elif char == '?':
			put_stderr("Accumulator: %d", acc)
			first_col = min(min(lowest_set(x) for x in field), x)
			last_col = max(max(bit_length(x) for x in field), x+1)
			first_row = min(next((i for i, v in enumerate(field) if v), inf), y)
			last_row = max(len(field) - next((i for i, v in enumerate(reversed(field)) if v), len(field)), y+1)
			for _y, val in enumerate(field[first_row:last_row], first_row):
				tmp = ""
				_x = first_col
				prev_here = False
				while _x < last_col:
					here = _x == x and _y == y
					if prev_here: tmp += ']'
					elif here: tmp += '['
					else: tmp += ' '
					tmp += chars[val>>_x&1]
					prev_here = here
					_x += 1
				if prev_here: tmp += ']'
				put_stderr(tmp)
		else:
			if char == '\n': line += 1
			char = None
		if char is not None:
			flush_debug('Executing: %r at [%d|%d] [%d -> %d]', \
			  char, x-xoff, y-yoff, oldacc, acc)
			
except KeyboardInterrupt:
	print >> sys.stderr, "Interrupted"
	sys.exit(1)
