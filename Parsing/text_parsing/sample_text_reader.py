from fileinput import input
from re import match

wanted_character = "TRUMP: "

dialogue = False
out = ""
for line in input():
    # match a dialogue header (5 tabs)
    result = match(r"^\t{5}(\S.*?)( *)$", line)
    if result:
        character = result.group(1)
        dialogue = (character == wanted_character)
        if not dialogue and len(out) > 0:
            # if speaker changed, print what we've got and start over
            print out
            out = ""
    elif dialogue:
        # match a spoken line (3 tabs)
        result = match(r"^\t{3}(\S.*?)([ \t]*?)$", line)
        if result:
            # append this line to the dialogue, with a space
            if len(out) > 0:
                out += " "
            out += result.group(1)

# just in case the input ends in the middle of dialogue
if len(out) > 0:
    print out