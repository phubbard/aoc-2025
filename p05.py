#!/usr/bin/env python3
from utils import get_all_data, log, assert_expr


def parse_data(inp_data: list) -> tuple:
    return 0,0


def part_one(fresh_ranges: list, ingredient_ids: list) -> int:
    return 0


def part_two(input_data: list) -> int:
    return 0


def test_part1():
    sample, full, answer, _ = get_all_data(5)
    # Split data into fresh ranges and ingredients
    fresh_ranges, ingredient_ids = parse_data(sample)
    score = part_one(fresh_ranges, ingredient_ids)
    assert_expr("str(score) == answer[0]")
    log.info("** Doing full dataset **")
    # if we got here, we can proceed to the full data set
    log.info(f'{part_one(full)=}')


def test_part2():
    sample, full, _, answer = get_all_data(5)

    score = part_two(sample)
    assert_expr("str(score) == answer[0]")
    log.info("** Doing full dataset **")
    # if we got here, we can proceed to the full data set
    log.info(f'{score=}')


if __name__ == '__main__':
    test_part1()
    test_part2()