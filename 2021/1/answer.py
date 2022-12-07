def part1(input):
    increases = 0
    prev_depth = int(input[0].strip())

    for i in range(1, len(input)):
        curr_depth = int(input[i].strip())

        if curr_depth > prev_depth:
            increases += 1
        
        prev_depth = curr_depth
    
    print('NUMBER OF INCREASES:', increases)
    return

def part2(input):
    increases = 0
    windows = {}

    for line in input:
        line = line.strip()
        values = line.split(' ')
        print(values)
    return

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    print('-----PART 1-----')
    part1(lines)
    print('-----PART 2-----')
    part2(lines)