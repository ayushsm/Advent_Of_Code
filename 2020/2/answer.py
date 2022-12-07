def part1(input):
    valid_passwords = 0
    for line in input:
        line = line.strip()
        number_of_times, target_letter, password = line.split(" ")

        target_letter = target_letter[:-1]
        min_number_of_times, max_number_of_times = number_of_times.split("-")
        min_number_of_times, max_number_of_times = int(min_number_of_times), int(max_number_of_times)

        seen = {}
        for letter in password:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1
            
        if target_letter in seen and (min_number_of_times <= seen[target_letter] <= max_number_of_times):
            valid_passwords += 1
    
    print('NUMBER OF VALID PASSWORDS:', valid_passwords)
    return

def part2(input):
    valid_passwords = 0
    for line in input:
        line = line.strip()
        positions, target_letter, password = line.split(" ")

        target_letter = target_letter[:-1]
        first_position, second_position = positions.split("-")
        first_position, second_position = int(first_position) - 1, int(second_position) - 1

        if (password[first_position] == target_letter) != (password[second_position] == target_letter): 
            valid_passwords += 1

    print('NUMBER OF VALID PASSWORDS:', valid_passwords)
    return

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    part1(lines)
    part2(lines)
