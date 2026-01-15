#!/usr/bin/env python3
from utils import get_all_data, log, assert_expr, product


def area(p1, p2):
    return product([abs(p1[x] - p2[x]) + 1 for x in range(len(p1))])


def find_all_areas(data: list) -> list:
    # Data struct is tuple of (a, b, area)
    log.info(f"computing all-pairs for {len(data)=}")
    areas = []
    for a_idx, a in enumerate(data):
        for b_idx, b in enumerate(data):
            areas.append((a, b, area(a, b)))
    return areas


def part_one(input_data: list) -> int:
    areas = find_all_areas(input_data)
    score = max(areas, key=lambda x: x[2])
    return score[2]



def part_two(input_data: list) -> int:
    return 0


def parse(inp_data: list) -> list:
    rc = []
    for row in inp_data:
        rs = row.split(',')
        rt = (int(rs[0]), int(rs[1]))
        rc.append(rt)

    return rc


def test_part1():
    r_sample, r_full, answer, _ = get_all_data(9)
    sample = parse(r_sample)
    full = parse(r_full)
    score = part_one(sample)
    log.info(f'sample {score=}')
    assert_expr("str(score) == answer[0]")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    score = part_one(full)
    log.info(f'full {score=}')


def test_part2():
    sample, full, _, answer = get_all_data(3)

    score = part_two(sample)
    assert_expr("str(score) == answer[0]")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    log.info(f'{score=}')


if __name__ == '__main__':
    test_part1()
    # test_part2()