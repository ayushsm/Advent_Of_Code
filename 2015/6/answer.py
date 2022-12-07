def part1(input):
    grid = {}
    for i in range(1000):
        for j in range(1000):
            grid[(i, j)] = 0

    for line in input:
        line = line.strip()
        words = line.split(' ')
        words = words[1:] if len(words) == 5 else words
        command = words[0]
        start_x, start_y = words[1].split(',')
        end_x, end_y = words[3].split(',')
 
        # print(start_x, start_y, end_x, end_y)
        if command == 'toggle':
            for x in range(int(start_x), int(end_x) + 1):
                for y in range(int(start_y), int(end_y) + 1):
                    if grid[(x, y)] == 1:
                        grid[(x, y)] = 0
                    else:
                        grid[(x, y)] = 1
        elif command == 'on':
            for x in range(int(start_x), int(end_x) + 1):
                for y in range(int(start_y), int(end_y) + 1):
                    grid[(x, y)] = 1
        else:
            for x in range(int(start_x), int(end_x) + 1):
                for y in range(int(start_y), int(end_y) + 1):
                    grid[(x, y)] = 0
        
    print('LIGHTS ON:', sum(grid.values()))

def part2(input):
    grid = {}
    for i in range(1000):
        for j in range(1000):
            grid[(i, j)] = 0

    for line in input:
        line = line.strip()
        words = line.split(' ')
        words = words[1:] if len(words) == 5 else words
        command = words[0]
        start_x, start_y = words[1].split(',')
        end_x, end_y = words[3].split(',')
        # print(start_x, start_y, end_x, end_y)

        if command == 'toggle':
            for x in range(int(start_x), int(end_x) + 1):
                for y in range(int(start_y), int(end_y) + 1):
                    grid[(x, y)] += 2
        elif command == 'on':
            for x in range(int(start_x), int(end_x) + 1):
                for y in range(int(start_y), int(end_y) + 1):
                    grid[(x, y)] += 1
        else:
            for x in range(int(start_x), int(end_x) + 1):
                for y in range(int(start_y), int(end_y) + 1):
                    grid[(x, y)] = max(grid[(x, y)] - 1, 0)

    print('LIGHTS ON:', sum(grid.values()))

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    # part1(lines)
    part2(lines)