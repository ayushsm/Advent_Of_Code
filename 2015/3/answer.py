def movement(ns, we, dir):
    if dir == '^':
        ns += 1
    elif dir == 'v':
        ns -= 1
    elif dir == '>':
        we += 1
    else:
        we -= 1
    
    return ns, we


def part1(input):
    for line in input:
        line = line.strip()

        previous_locations = {(0, 0): 1}
        ns_location = 0
        we_location = 0
        presents = 1

        for dir in line:
            ns_location, we_location = movement(ns_location, we_location, dir)
            curr_location = (ns_location, we_location)
            if curr_location not in previous_locations:
                 presents += 1
            
            previous_locations[curr_location] = 1

        print('TOTAL PRESENTS DELIVERED:', presents)

NUMBER_OF_SANTAS = 2

def part2(input):
    for line in input:
        line = line.strip()

        presents = 1
        prev_locations = {(0, 0): 1}
        santa_directory = {i: (0, 0) for i in range(NUMBER_OF_SANTAS)}
        curr_santa = 0

        for dir in line:
            curr_ns, curr_we = santa_directory[curr_santa]
            curr_ns, curr_we = movement(curr_ns, curr_we, dir)

            curr_loc = (curr_ns, curr_we)
            if curr_loc not in prev_locations:
                presents += 1

            prev_locations[curr_loc] = 1
            santa_directory[curr_santa] = curr_loc

            curr_santa = (curr_santa + 1) % NUMBER_OF_SANTAS

        print('TOTAL PRESENTS DELIVERED:', presents)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    # part1(lines)
    part2(lines)