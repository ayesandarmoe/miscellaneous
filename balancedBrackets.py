#!/bin/python
#
#https://www.hackerrank.com/challenges/balanced-brackets/problem

import sys

brackets = {
    ')' : '(', ']' : '[' , '}' : '{'
}

t = int(raw_input().strip())
for a0 in xrange(t):
    rb = list()
    s = raw_input().strip()
    if len(s) % 2 != 0:
        print "NO"
    else:
        #balanced = True
        for i in xrange(len(s)):
            if brackets.has_key(s[i]): # if this is right bracket
                if len(rb) > 0:
                    lb = rb.pop()
                    if lb != brackets.get(s[i]):
                        rb.append(lb)
                        rb.append(s[i])
                else:
                    rb.append(s[i])

                
            else: # this is a left bracket, then put it in a stack
                rb.append(s[i])
        if len(rb) == 0:
            print "YES"
        else:
            print "NO"

