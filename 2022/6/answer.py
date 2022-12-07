TOTAL_DISK_SPACE = 70000000
NEEDED_SPACE = 30000000

def part1(input):
    curr_dir = "/"
    parent_dictionary = {"/": "/"}
    children_dictionary = {"/": []}

    idx = 0
    while idx < len(input):
        line = input[idx].strip()
        base_commands = line.split(' ')

        if base_commands[1] == "cd":
            if base_commands[2] == "/":
                curr_dir = "/"
            elif base_commands[2] == "..":
                curr_dir = parent_dictionary[curr_dir]
            else:
                curr_dir = curr_dir + "/" + base_commands[2]
            
            idx += 1
        elif base_commands[1] == "ls":
            idx += 1
            while idx < len(input):
                command = input[idx].strip().split(" ")
                if command[0] == "$":
                    break
                
                target_dir = curr_dir + "/" + command[1]
                parent_dictionary[target_dir] = curr_dir
                # print(curr_dir, children_dictionary[curr_dir])
                children_dictionary[curr_dir].append(target_dir)

                if command[0] == "dir":
                    children_dictionary[target_dir] = []
                else:
                    children_dictionary[target_dir] = int(command[0])

                idx += 1

    dir_sizes = {}
    for key, value in children_dictionary.items():
        dfs(children_dictionary, key, dir_sizes)

    total_value = 0
    for value in dir_sizes.values():
        total_value += value if value <= 100000 else 0
    print('OUTPUT:', total_value)
    
    return dir_sizes

def dfs(directory_list, curr_dir, cache):
    total_sum = 0
    if curr_dir in cache:
        return cache[curr_dir]
    if type(directory_list[curr_dir]) == int:
        return directory_list[curr_dir]
    else:
        for key in directory_list[curr_dir]:
            total_sum += dfs(directory_list, key, cache)
        cache[curr_dir] = total_sum
    return total_sum

def part2(input):
    dir_sizes = part1(input)
    sizes = dir_sizes.values()
    sorted_sizes = sorted(sizes)

    current_unused_space = TOTAL_DISK_SPACE - dir_sizes['/']
    current_needed_space = NEEDED_SPACE - current_unused_space

    low = 0
    high = len(sorted_sizes)

    while low < high:
        mid = (low + high) // 2

        if sorted_sizes[mid] == current_needed_space:
            break
        elif sorted_sizes[mid] < current_needed_space:
            low = mid + 1
        else:
            high = mid - 1

    while mid < len(sorted_sizes) and sorted_sizes[mid] < current_needed_space:
        mid += 1

    # print('-NEEDED DIRECTORY SIZE:', current_needed_space)
    print('DELETED DIRECTORY SIZE:', sorted_sizes[mid])
    return

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    print('-----PART 1-----')
    part1(lines)
    print('-----PART 2-----')
    part2(lines)