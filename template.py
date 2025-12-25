#!/usr/bin/env python3
from utils import get_all_data, log, assert_expr


def part_one(input_data: list) -> int:
    return 0


def part_two(input_data: list) -> int:
    return 0


def test_part1():
    sample, full, answer, _ = get_all_data(3)
    score = part_one(sample)
    assert_expr("str(score) == answer[0]")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    log.info(f'{part_one(full)=}')


def test_part2():
    sample, full, _, answer = get_all_data(3)

    score = part_two(sample)
    assert_expr("str(score) == answer[0]")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    log.info(f'{score=}')


if __name__ == '__main__':
    test_part1()
    test_part2()