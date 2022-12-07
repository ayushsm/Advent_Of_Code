def part1(input):
    total_area = 0

    for line in input:
        l, w, h = [int(_) for _ in line.split('x')]
        lw = l * w
        lh = l * h
        wh = w * h
        min_side = min(lw, lh, wh)
        total_area += 2 * lw + 2 * lh + 2 * wh + min_side

    print('TOTAL AREA:', total_area)

def part2(input):
    total_length = 0

    for line in input:
        l, w, h = [int(_) for _ in line.split('x')]
        min_side = min(l, w, h)
        if min_side == l:
            second_min_side = min(w, h)
        elif min_side == w:
            second_min_side = min(l, h)
        else:
            second_min_side = min(l, w)
        total_length += 2 * min_side + 2 * second_min_side + l * w * h

    print('TOTAL LENGTH:', total_length)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    # part1(lines)
    part2(lines)