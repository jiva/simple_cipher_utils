#!/usr/bin/python

# xor by a byte or bruteforce all - jiva
# bruteforce all 255: ./xor.py <input_file>
# xor against a byte: ./xor.py <input_file> <ord_byte_value>

import sys

f = open(sys.argv[1]).read()

if len(sys.argv) == 3:
	fw = open('_xor' + sys.argv[2] + '.bin', 'wb')
	for c in f:
		fw.write(chr(ord(c) ^ int(sys.argv[2])))
	fw.close()
else:
	for i in xrange(256):
		fw = open('_xor' + str(i) + '.bin', 'wb')
		for c in f:
			fw.write(chr(ord(c) ^ i))
		fw.close()

