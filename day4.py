"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-
thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5
hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must
find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

 - If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes
 (000001dbbfa...), and it is the lowest such number to do so.
 - If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is
 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

Your puzzle input is ckczppom.


*************** NOTE: Part 2 will take some time to execute ********************
"""
import hashlib


def find_lowest_md5_hash(key, zeros):

    i = -1
    zerosstring = "0" * zeros
    hashresult = "000000000000000"

    while not (hashresult[:zeros] == zerosstring) or hashresult[zeros] == "0":
        i += 1
        hashresult = hashlib.md5(key + str(i)).hexdigest()

    return [hashresult, i]

if __name__ == "__main__":
    keys = ["abcdef", "pqrstuv", "ckczppom"]

    print "Part 1"
    for key in keys:
        print "Key " + str(key) + ": " + str(find_lowest_md5_hash(key, 5))

    print "Part 2"
    for key in keys:
        print "Key " + str(key) + ": " + str(find_lowest_md5_hash(key, 6))

