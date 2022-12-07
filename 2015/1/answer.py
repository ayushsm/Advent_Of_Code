def part1(input):
    for line in input:
        floor = 0
        line = line.strip()
        for _ in line:
            if _ == "(":
                floor += 1
            else:
                floor -= 1
        
        print('FLOOR:', floor)

        floor = 0

TARGET_FLOOR = -1

def part2(input):
    for line in input:
        floor = 0
        line = line.strip()
        for idx, _ in enumerate(line):
            if _ == "(":
                floor += 1
            else:
                floor -= 1

            print(floor)
            if floor == TARGET_FLOOR:
                print('FIRST BASEMENT:', idx + 1)
                break

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    # part1(lines)
    part2(lines)