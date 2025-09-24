#!/usr/bin/python

# Convert a string to a 2DFuck program outputting that string
# The -n switch removes the trailing newline
# It assumes that the accumulator is 0 at the beginning, so add/remove a '!' at the beginning
# it it isn't. It tells you what the accumulator is set to in the end.

import getopt, sys

try: opts, args = getopt.getopt(sys.argv[1:], 'n')
except getopt.GetoptError:
	print >> sys.stderr, 'Usage: %s [-n] [<string>]' % sys.argv[0]
	sys.exit(1)

tty = sys.stdout.isatty()

if args: arg = ' '.join(args)
elif tty: arg = input('Enter string: ')
else:
	if sys.stdin.isatty(): print >> sys.stderr, 'Enter string: ',
	arg = input()

if '-n' not in (x[0] for x in opts): arg += '\n'

if tty: result = 'Program: '
else: result = ''

acc = 0

for i in arg:
	char = ord(i)
	x = 8
	while x:
		x -= 1
		bit = char >> x & 1
		if bit != acc:
			result += '!'
			acc = bit
		result += '.'

print (result)
print >> sys.stderr, "Accumulator at the end: %d" % acc
