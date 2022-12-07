def part1(input):
    for line in input:
        line = line.strip()
        total = 0
        
        for idx, digit in enumerate(line):
            if digit == line[idx - 1]:
                total += int(digit)

        print('SUM:', total)

    return

def part2(input):
    for line in input:
        line = line.strip()
        total = 0
        half_line_len = len(line) // 2

        for idx, digit in enumerate(line[:half_line_len]):
            if digit == line[idx + half_line_len]:
                total += 2 * int(digit)
            
        print('SUM:', total)

    return

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    print('-----PART 1-----')
    part1(lines)
    print('-----PART 2-----')
    part2(lines)