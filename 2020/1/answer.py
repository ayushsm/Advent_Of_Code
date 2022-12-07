def part1(input):
    seen = {}
    for line in input:
        line = line.strip()
        number = int(line)

        if 2020 - number in seen:
            print('OUTPUT:', number * (2020 - number))
            return
        seen[number] = 1

    print('NOT FOUND')
    return

def part2(input):
    inputs = []
    for line in input:
        line = line.strip()
        number = int(line)
        inputs.append(number)
    inputs = sorted(inputs)
    inputs_len = len(inputs)

    for i, num in enumerate(inputs[:-2]):
        target = 2020 - num
        j = i + 1
        k = inputs_len - 1

        while j < k:
            j_val = inputs[j]
            k_val = inputs[k]

            if j_val + k_val == target:
                print('OUTPUT:', num * j_val * k_val, num, j_val, k_val)
                return
            elif j_val + k_val < target:
                j += 1
            else:
                k -= 1
        
    print('NO OUTPUT')
    return

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    print('-----PART 1-----')
    part1(lines)
    print('-----PART 2-----')
    part2(lines)