def part1(lines):
    covered = 0
    for line in lines:
        line = line.strip()
        range1, range2 = line.split(',')

        range1, range2 = range1.split('-'), range2.split('-')

        start1, end1 = int(range1[0]), int(range1[1])
        start2, end2 = int(range2[0]), int(range2[1])

        if (start2 <= start1 and end2 >= end1) or (start1 <= start2 and end1 >= end2):
            covered += 1

    print('RANGES COVERED:', covered) 

def part2(input):
    overlap = 0
    for line in lines:
        line = line.strip()
        range1, range2 = line.split(',')
        range1, range2 = range1.split('-'), range2.split('-')

        start1, end1 = int(range1[0]), int(range1[1])
        start2, end2 = int(range2[0]), int(range2[1])

        if (start1 <= end2 and end1 >= end2) or (start2 <= end1 and end2 >= end1) or (start1 <= start2 and end1 >= start2) or (start2 <= start1 and end2 >= start1):
            overlap += 1

    print('OVERLAPPING RANGES:', overlap)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    part1(lines)
    part2(lines)