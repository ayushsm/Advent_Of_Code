import math

def part1(input):
    total_sum = 0
    for line in input:
        line = line.strip()
        number = int(line)
        total_sum += math.floor(number / 3) - 2

    print('TOTAL:', total_sum)
    return

def part2(input):
    total_sum = 0
    for line in input:
        line = line.strip()
        number = int(line)

        while number > 0:
            number = max(math.floor(number / 3) - 2, 0)
            total_sum += number
    
    print('TOTAL:', total_sum)
    return

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    print('-----PART 1-----')
    part1(lines)
    print('-----PART 2-----')
    part2(lines)