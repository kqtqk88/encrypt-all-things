#!/usr/bin/python
import sys

''' Caesar cipher implementation in python '''

'''
# takes first arg and prints it
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv[1])
'''
if len(sys.argv) < 2:

    print("enter a valid input")
else: 

    out = ''

    for c in sys.argv[1]:
        c = chr(ord(c) + 3)
        out = out + c

    print out
