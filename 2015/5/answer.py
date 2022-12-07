VOWELS = 'aeiou'
ILLEGAL_STRINGS = {'ab': 1, 'cd': 1, 'pq': 1, 'xy': 1}

def part1(input):
    nice_strings = 0

    for line in input:
        line = line.strip()
        number_of_vowels = 0
        illegal = 0
        prev_letter = ''
        duplicate = 0

        for letter in line:
            if letter in VOWELS:
                number_of_vowels += 1
            if letter == prev_letter:
                duplicate += 1
            if prev_letter + letter in ILLEGAL_STRINGS:
                illegal = 1
                break

            prev_letter = letter

        if number_of_vowels >= 3 and duplicate >= 1 and illegal == 0:
            nice_strings += 1

    print('NUMBER OF NICE STRINGS:', nice_strings)

def part2(input):
    nice_strings = 0

    for line in input:
        line = line.strip()
        middle_letter = 0
        duplicate = 0
        pairs = {}
        prev_letter = ''

        for idx, letter in enumerate(line):
            if idx > 1 and letter == line[idx - 2]:
                middle_letter += 1
            if idx > 0:
                pair = prev_letter + letter

                if pair in pairs:
                    if pairs[pair] < idx - 1:
                        duplicate += 1
                else:
                    pairs[pair] = idx

            prev_letter = letter

            
        if duplicate >= 1 and middle_letter >= 1:
            nice_strings += 1
            
    print('NUMBER OF NICE STRINGS:', nice_strings)



if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    # part1(lines)
    part2(lines)