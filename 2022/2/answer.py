RPS_PART1_PLAY_MAPPING = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3
    }
}

RPS_PART1_SCORE_MAPPING = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

RPS_PART2_PLAY_MAPPING = {
    'X': {
        'A': 3,
        'B': 1,
        'C': 2
    },
    'Y': {
        'A': 1,
        'B': 2,
        'C': 3
    },
    'Z': {
        'A': 2,
        'B': 3,
        'C': 1
    }
}

RPS_PART2_SCORE_MAPPING = {
    'X': 0,
    'Y': 3,
    'Z': 6
}



def part1(input):
    total_sum = 0

    for line in input:
        # print(line.strip())
        opp_play, my_play = line.strip().split(' ')
        # print(opp_play, my_play, RPS_MAPPING[opp_play][my_play])
        total_sum += RPS_PART1_PLAY_MAPPING[my_play][opp_play] + RPS_PART1_SCORE_MAPPING[my_play]

    print('TOTAL SCORE:', total_sum)

def part2(input):
    total_sum = 0

    for line in input:
        # print(line.strip())
        opp_play, my_play = line.strip().split(' ')
        # print(opp_play, my_play, RPS_MAPPING[opp_play][my_play])
        total_sum += RPS_PART2_PLAY_MAPPING[my_play][opp_play] + RPS_PART2_SCORE_MAPPING[my_play]

    print('TOTAL SCORE:', total_sum)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    # part1(lines)
    part2(lines)
