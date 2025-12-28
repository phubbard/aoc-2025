from utils import Data2D, log, assert_expr


START = 'S'
SPLITTER = '^'
BLANK = '.'
BEAM = '|'


def findall(inp: str, character: str) -> list:
    rc = []
    cur_start = 0
    while True:
        tmp = inp.find(character, cur_start)
        if tmp < 0:
            break
        rc.append(tmp)
        cur_start = tmp + 1
        if cur_start >= len(inp):
            break
    return rc


def as_str(inp: list) -> str:
    return ''.join(inp)


def part_one(sample: bool) -> int:
    data = Data2D()
    data.load(7, sample=sample, strip=True)
    data.add_padding(BLANK)
    # print(sample)

    # Find starting point
    start_col = as_str(data[1]).index(START)
    data[2][start_col] = BEAM

    score = 0
    for idx in range(2, data.num_rows() - 1):
        # print(sample)
        splitters = findall(as_str(data[idx]), SPLITTER)

        for splitter in splitters:
            if data[idx - 1][splitter] == BEAM:
                score += 1
                if data[idx - 1][splitter - 1] == BLANK:
                    data[idx][splitter - 1] = BEAM

                if data[idx - 1][splitter + 1] == BLANK:
                    data[idx][splitter + 1] = BEAM
        # print(idx,sba)

        beams = findall(as_str(data[idx]), BEAM)
        for beam in beams:
            if data[idx + 1][beam] == BLANK:
                data[idx + 1][beam] = BEAM

    log.info(f"sample {score=}")
    return score


if __name__ == '__main__':
    part_one(True)
    part_one(False)