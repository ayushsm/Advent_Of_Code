def part1(lines):
    wires = {}

    for line in lines:
        line = line.strip()
        input, output = line.split('->')
        input, output = input.strip(), output.strip()
        input = input.split(' ')
        
        if len(input) == 1:
            wires[output] = int(input[0])
        elif len(input) == 2:
            print(input)
            input_wire = input[1]
            wires[output] = ~wires[input_wire]
        else:
            input1, command, input2 = input
            if command == 'AND':
                wires[output] = wires[input1] & wires[input2] 
            elif command == 'OR':
                wires[output] = wires[input1] | wires[input2]
            elif command == 'LSHIFT':
                wires[output] = wires[input1] << int(input2)
            else:
                wires[output] = wires[input1] >> int(input2)

        if wires[output] < 0:
            wires[output] += 2 ** 16
    print(wires)

# def part2(input):

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    part1(lines)
    # part2(lines)