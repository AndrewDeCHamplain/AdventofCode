"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

  - > delivers presents to 2 houses: one at the starting location, and one to the east.
  - ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
  - ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

  - ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
  - ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
  - ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

"""

def findHousesVisited(directions, workers):

    # Each worker starts at the same spot (arbitrarily set to zero)
    x = [0] * workers
    y = [0] * workers

    # Before instructions are followed, the starting house is delivered a present
    visited = [(0,0)]

    # Each worker takes an instruction in turn
    worker = 0

    for step in directions:

        worker = ( worker + 1 ) %  workers

        # Move the worker according to their instruction
        if step == 'v':
            y[worker] += 1
        elif step == '^':
            y[worker] -= 1
        elif step == '>':
            x[worker] += 1
        elif step == '<':
            x[worker] -= 1
        else:
            print "Error: step not recognised"

        # We want the number of houses visited at least once by any worker
        if (x[worker], y[worker]) not in visited:
            visited.append( (x[worker], y[worker]) )

    print "Number of houses visited with {} worker: {}".format( workers, len(visited) )

if __name__ == "__main__":

    text_file=open("inputday3_1.txt", "r")
    lines = text_file.readlines()
    directions = list(lines[0])

    # Part 1: 1 worker delivers presents
    findHousesVisited( directions, 1 )

    # Part 2: 1 worker delivers presents
    findHousesVisited( directions, 2 )
