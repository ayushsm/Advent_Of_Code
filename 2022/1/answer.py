def part1(input):
    curr_sum = 0
    max_sum = 0
    for line in input:
        if line == '\n':
            print('ELF CALORIES:', curr_sum)
            curr_sum, max_sum = base_case(curr_sum, max_sum)
        else:
            line = line.strip()
            curr_sum += int(line) 
    
    if curr_sum > 0:
        curr_sum, max_sum = base_case(curr_sum, max_sum)
        
    print('MAX CALORIES:', max_sum)

def part2(input):
    curr_sum = 0
    max_sum = 0
    second_max_sum = 0
    third_max_sum = 0

    for line in input:
        if line == '\n':
            print('ELF CALORIES:', curr_sum)
            if curr_sum >= max_sum:
                third_max_sum = second_max_sum
                second_max_sum = max_sum
                max_sum = curr_sum
            elif curr_sum >= second_max_sum:
                third_max_sum = second_max_sum
                second_max_sum = curr_sum
            elif curr_sum >= third_max_sum:
                curr_sum, third_max_sum = base_case(curr_sum, third_max_sum)
            curr_sum = 0
        else:
            line = line.strip()
            curr_sum += int(line) 

    if curr_sum > 0:
        if curr_sum >= max_sum:
            third_max_sum = second_max_sum
            second_max_sum = max_sum
            max_sum = curr_sum
        elif curr_sum >= second_max_sum:
            third_max_sum = second_max_sum
            second_max_sum = curr_sum
        elif curr_sum >= third_max_sum:
            curr_sum, third_max_sum = base_case(curr_sum, third_max_sum)        

    print('TOP 3 TOTAL CALORIES:', max_sum + second_max_sum + third_max_sum)
    
def base_case(curr_sum, max_sum):
    max_sum = max(max_sum, curr_sum)
    curr_sum = 0
    return curr_sum, max_sum


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    # part1(lines)
    part2(lines)