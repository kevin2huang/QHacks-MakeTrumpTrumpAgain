#!usr/bin/python
import re

with open('abc_text.txt') as f:
	lines = [x.strip('\n') for x in f.readlines()]


def parse_txt(str_line, index, flag, txt_file):
	if index < len(str_line):
		matchObj = re.match( r'([A-Z]{3,}):', str_line[index])
		matchObj2 = re.match( r'[(]', str_line[index])
		if matchObj and matchObj.group() == 'TRUMP:':
			txt_file.write(str_line[index].replace("TRUMP: ","",1) + "\n")
			flag = True

		elif matchObj2:
			pass

		elif flag and not ((matchObj and matchObj.group() != 'TRUMP:') or matchObj2) :
			txt_file.write(str_line[index] + "\n")

	#	elif (matchObj and matchObj.group() != 'TRUMP:') or matchObj2:
		else:
			flag = False

		parse_txt(str_line, index + 1, flag, txt_file)

	else:
		txt_file.write(" ")
#		parse_txt(str_line, index + 1, flag)


# Function call
txt_file = open('output_text.txt', 'w')
parse_txt(lines, 1, True, txt_file)
txt_file.close()

#parse_txt(lines, 1, True)