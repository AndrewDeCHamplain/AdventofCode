"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

- It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
- It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
- It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

- ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
- aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
- jchzalrnumimnmhp is naughty because it has no double letter.
- haegwjzuvuyypxyu is naughty because it contains the string xy.
- dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?
"""


def nice_strings(lines):

    vowels = "aeoiu"
    badcombos = ["ab", "cd", "pq", "xy"]
    nice_strings = 0

    for line in lines:

        if not any(char in line for char in badcombos):
            vowelcount = 0
            same_in_row = False

            for letter in line:
                if letter in vowels:
                    vowelcount += 1
                if letter*2 in line:
                    same_in_row = True
            if vowelcount >= 3 and same_in_row:
                nice_strings += 1
    print nice_strings


if __name__ == "__main__":
    text_file=open("inputday5.txt", "r")
    lines = text_file.readlines()

    print "Part 1"
    nice_strings(lines)