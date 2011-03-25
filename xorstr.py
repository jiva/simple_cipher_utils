#!/usr/bin/python

# xor against a multibyte key - jiva
# usage: ./xorstr.py <input_file> <key>

import sys

f = open(sys.argv[1]).read()

xorstr = sys.argv[2]

fw = open('_xorstr.bin', 'wb')
for i in xrange(len(f)):
	fw.write(chr(ord(f[i]) ^ ord(xorstr[i % len(xorstr)-1])))
fw.close()

