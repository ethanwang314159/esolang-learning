#!/usr/bin/python

# Remove all comments from a 2DFuck program (all characters that do not have a meaning)
# Usage (bash): remove_comments.py < infile > outfile

import sys

sys.stdout.write(''.join(x for x in sys.stdin.read() if x in '<>^v!rx.,[]l'))
