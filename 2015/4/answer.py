import hashlib
import sys

PART1_NUMBER_OF_ZEROES = 5
PART2_NUMBER_OF_ZEROES = 6

def part1(input):
    zero_string = '0' * PART1_NUMBER_OF_ZEROES
    for line in input:
        line = line.strip()
        for n in range(sys.maxsize):
            val = line + str(n)
            hashed_val = hashlib.md5(val.encode()).hexdigest()
            if hashed_val[:PART1_NUMBER_OF_ZEROES] == zero_string:
                print('VALUE:', n)
                break

def part2(input):
    zero_string = '0' * PART2_NUMBER_OF_ZEROES

    for line in input:
        line = line.strip()
        for n in range(sys.maxsize):
            val = line + str(n)
            hashed_val = hashlib.md5(val.encode()).hexdigest()
            if hashed_val[:PART2_NUMBER_OF_ZEROES] == zero_string:
                print('VALUE:', n)
                break

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    # part1(lines)
    part2(lines)