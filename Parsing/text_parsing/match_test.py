#!usr/bin/python

import re

line = "TRUMP: Well look, he was a failed candidate, he should have beaten president Obama very easy."
line2 = "(asdfalskd)"

#matchObj = re.match( r'([A-Z]{3,}):', line)
matchObj = re.match( r'[(]', line2)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
else:
   print "No match!!"