#!/usr/bin/env python

# print byte frequencies - jiva
# usage: ./bytehist.py <input_file>

import sys, operator

f = open(sys.argv[1]).read()

d = {}

for c in f:
	if ord(c) in d: d[ord(c)] += 1
	else: d[ord(c)] = 1

sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1))

print 'byte','\t', 'freq'
for tup in sorted_d:
	print tup[0],'\t',tup[1]

