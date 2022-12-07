def part1(input):
    line_len = len(input[0])
    stacks = {i: [] for i in range(1, line_len // 4 + 1)}
    for line in input[:len(stacks)]:
        idx = 0
        count = 1
        while idx < line_len - 1:
            if line[idx] != " ":
                stacks[count].insert(0, line[idx + 1])
            
            count += 1
            idx += 4

    for line in input[len(stacks) + 1:]:
        line = line.strip()
        instr = line.split(" ")

        number_to_move = int(instr[1])
        col_from = int(instr[3])
        col_to = int(instr[5])

        while number_to_move > 0:    
            val = stacks[col_from].pop()
            stacks[col_to].append(val)

            number_to_move -= 1
        
    print('FINAL STACKS:', stacks)
    return
    
def part2(input):
    line_len = len(input[0])
    stacks = {i: [] for i in range(1, line_len // 4 + 1)}
    for line in input[:len(stacks)]:
        idx = 0
        count = 1
        while idx < line_len - 1:
            if line[idx] != " ":
                stacks[count].insert(0, line[idx + 1])
            
            count += 1
            idx += 4

    for line in input[len(stacks) + 1:]:
        line = line.strip()
        instr = line.split(" ")

        number_to_move = int(instr[1])
        col_from = int(instr[3])
        col_to = int(instr[5])

        stacks[col_from], section_moved = stacks[col_from][:-number_to_move], stacks[col_from][-number_to_move:]
        stacks[col_to] += section_moved

    print('FINAL STACKS:', stacks)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    part1(lines)
    part2(lines)