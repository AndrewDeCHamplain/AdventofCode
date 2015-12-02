"""
--- Part Two ---

Now, given the same instructions, find the position of the first character that causes him to
enter the basement (floor -1). The first character in the instructions has position 1, the second
character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?
"""

text_file=open("inputday1_1.txt", "r")
lines = text_file.readlines()
floor = 0
position = 0

for line in lines[0]:
    position += 1
    if line == "(":
        floor += 1
    elif line == ")":
        floor -= 1

    if floor < 0:
        break
print position
