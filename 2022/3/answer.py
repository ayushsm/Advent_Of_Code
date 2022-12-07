def part1(input):
    score = 0

    for line in input:
        line = line.strip()
        line_len = len(line)
        half_line_len = line_len // 2

        part1_set = set(line[:half_line_len])
        part2_set = set(line[half_line_len:])

        common_item = part1_set.intersection(part2_set).pop()
        # print(common_item)
        print(common_item, ord(common_item))
        if common_item == common_item.upper():
            score += ord(common_item) - 64 + 26
        else:
            score += ord(common_item) - 96
    
    print('FINAL SCORE:', score)

def part2(input):
    score = 0

    curr_set = set()
    line_count = 0
    for line in input:
        if line_count == 3:
            common_item = curr_set.pop()
            if common_item == common_item.upper():
                score += ord(common_item) - 64 + 26
            else:
                score += ord(common_item) - 96
            
            line_count = 0

        line = line.strip()      
        if not curr_set:
            curr_set = set(line)
        else:
            line_set = set(line)
            curr_set = line_set.intersection(curr_set)
        line_count += 1

    common_item = curr_set.pop()
    if common_item == common_item.upper():
        score += ord(common_item) - 64 + 26
    else:
        score += ord(common_item) - 96

    print('FINAL SCORE:', score)
            

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    # part1(lines)
    part2(lines)
