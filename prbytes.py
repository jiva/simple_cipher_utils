#!/usr/bin/env python

# simplified hexdump: print hex-encoded bytes from input file - jiva
# usage: ./prbytes.py <input_file>

import sys

f = open(sys.argv[1]).read()

for b in f:
	if len(hex(ord(b))[2:]) == 2:
		print hex(ord(b))[2:],
	else:
		print '0' + hex(ord(b))[2:],
