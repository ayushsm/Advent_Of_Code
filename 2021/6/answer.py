PART1_MARKER_COUNT = 4
PART2_MARKER_COUNT = 14

def part1(input, marker_count):
    for line in input:
        seen = {}
        for idx, char in enumerate(line):
            if idx >= marker_count:
                prev_char = line[idx - marker_count]
                seen[prev_char] -= 1
                if seen[prev_char] <= 0:
                    del seen[prev_char]
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1

            if len(seen) == marker_count:
                # print(seen)
                print('MARKER AT:', idx + 1)
                break

    # print('NO MARKER FOUND')                
    return

def part2(input):
    part1(input, PART2_MARKER_COUNT)
    return

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    print('-----PART 1-----')
    part1(lines, PART1_MARKER_COUNT)
    print('-----PART 2-----')
    part2(lines)