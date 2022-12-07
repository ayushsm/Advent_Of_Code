def part1(input):
    for line in input:
        ns = 0
        we = 0
        curr_dir = "N"

        instructions = line.split(", ")

        for inst in instructions:
            turn = inst[0]
            mag = int(inst[1:])

            if turn == "R":
                if curr_dir == "N":
                    curr_dir = "E"
                    we += mag
                elif curr_dir == "E":
                    curr_dir = "S"
                    ns -= mag
                elif curr_dir == "S":
                    curr_dir = "W"
                    we -= mag
                else:
                    curr_dir = "N"
                    ns += mag
            else:
                if curr_dir == "N":
                    curr_dir = "W"
                    we -= mag
                elif curr_dir == "E":
                    curr_dir = "N"
                    ns += mag
                elif curr_dir == "S":
                    curr_dir = "E"
                    we += mag
                else:
                    curr_dir = "S"
                    ns -= mag
        
        print("DISTANCE:", abs(ns) + abs(we))
    return

def part2(input):
    for line in input:
        seen = {}
        curr_dir = "N"
        curr_pos = [0, 0]

        instructions = line.split(", ")

        for inst in instructions:
            turn = inst[0]
            mag = int(inst[1:])

            if turn == "R":
                if curr_dir == "N":
                    curr_dir = "E"
                elif curr_dir == "E":
                    curr_dir = "S"
                elif curr_dir == "S":
                    curr_dir = "W"
                else:
                    curr_dir = "N"
            else:
                if curr_dir == "N":
                    curr_dir = "W"
                elif curr_dir == "E":
                    curr_dir = "N"
                elif curr_dir == "S":
                    curr_dir = "E"
                else:
                    curr_dir = "S"

            curr_pos = movement(curr_dir, curr_pos, mag, seen)
            if seen[tuple(curr_pos)] > 1:
                print('FIRST REVISITED LOCATION DISTANCE:', abs(curr_pos[0])+ abs(curr_pos[1]))
                return
    return

def movement(curr_dir, curr_pos, mag, seen):
    for _ in range(mag):
        if curr_dir == "N":
            curr_pos[1] += 1
        elif curr_dir == "E":
            curr_pos[0] += 1
        elif curr_dir == "S":
            curr_pos[1] -= 1
        else:
            curr_pos[0] -= 1

        tuple_pos = tuple(curr_pos)
        if tuple_pos in seen:
            seen[tuple_pos] += 1
            return curr_pos
        
        seen[tuple_pos] = 1

    return curr_pos

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    part1(lines)
    part2(lines)