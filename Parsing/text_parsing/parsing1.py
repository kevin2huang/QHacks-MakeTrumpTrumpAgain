#!usr/bin/python
import re

with open('abc_text.txt') as f:
    lines = [x.strip('\n') for x in f.readlines()]
    

def parse_txt(str_line, index, flag):
	if index < len(str_line):
		matchObj = re.match( r'([A-Z]{3,}):', str_line[index])
		matchObj2 = re.match( r'[(]', str_line[index])
		if matchObj and matchObj.group() == 'TRUMP:':
			print (str_line[index].replace("TRUMP: ","",1))
			flag = True
			parse_txt(str_line, index + 1, flag)

		elif matchObj2:
			parse_txt(str_line, index + 1, flag)

		elif flag and not ((matchObj and matchObj.group() != 'TRUMP:') or matchObj2) :
			print (str_line[index])
			parse_txt(str_line, index + 1, flag)

	#	elif (matchObj and matchObj.group() != 'TRUMP:') or matchObj2:
		else:
			flag = False
			parse_txt(str_line, index + 1, flag)
	else:
		print(" ")
#		parse_txt(str_line, index + 1, flag)


# Function call
parse_txt(lines, 0, True)