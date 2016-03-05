#!usr/bin/python

import re

with open('abc_text.txt') as f:
    lines = [x.strip('\n') for x in f.readlines()]

print lines