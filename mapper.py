#!/usr/bin/env python
import sys
import string


# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    line = line.lower()
    line = line.translate(string.maketrans("",""), string.punctuation)

    # split the line into words; splits on any whitespace
    words = line.split()

    stopwords = set(['the','and'])
    
    for word in words:
         if word not in stopwords:
              print '%s\t%s' % (word, "1")

