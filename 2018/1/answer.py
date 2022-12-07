def part1(input):
    frequency = 0
    for line in input:
        line = line.strip()
        # shifts = line.split(', ')

        # for shift in shifts:
        pos_or_neg = line[0]
        mag = int(line[1:])
        frequency += mag if pos_or_neg == '+' else -1 * mag

    print('TOTAL FREQUENCY:', frequency)
    return

def part2(input):
    frequency = 0
    found = 0
    seen = {0: 1}

    while not found:
        for line in input:
            line = line.strip()
            # shifts = line.split(', ')
    
                # for shift in shifts:
            pos_or_neg = line[0]
            mag = int(line[1:])
            frequency += mag if pos_or_neg == '+' else -1 * mag
        
            if frequency in seen:
                found = 1
                break
                    
            seen[frequency] = 1
        
    print('FREQUENCY:', frequency)
    return

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    print('-----PART 1-----')
    part1(lines)
    print('-----PART 2-----')
    part2(lines)