#!/usr/bin/env python3

from utils import get_all_data, log, assert_expr
import re


def parse_ranges(input: str) -> list:
    # Parse '11-22,95-115' into [[11, 22], [95-115]]
    ranges = input.split(',')
    rc = []
    for item in ranges:
        tmp = item.split('-')
        rc.append([int(tmp[0]), int(tmp[1])])
    log.debug(f'{len(rc)=}')
    return rc


def is_invalid(id: int) -> bool:
    id_str = str(id)
    if len(id_str) % 2 != 0:
        # All invalid IDs have even numbers of digits
        return False
    num_digits = len(id_str)
    num_to_check = int(num_digits / 2)
    for idx in range(num_to_check):
        lvalue = id_str[idx]
        rvalue = id_str[idx + num_to_check]
        if lvalue != rvalue:
            return False
    return True


regexes = [
    r"(\d+)\1",
    r"(\d{2,})\1",
    r"(\d{3,})\1",
    r"(\d{4,})\1",
    r"(\d{5,})\1",
    r"(\d{6,})\1",
    r"(\d{7,})\1",
    r"(\d{8,})\1",
    r"(\d{9,})\1",
    r"(\d{10,})\1",
]

matchers = [re.compile(item) for item in regexes]


def is_invalid_two(id: int) -> bool:
    id_str = str(id)

    # Loop, increasing the number of digits that need to match.
    match_len = 2
    for matcher in matchers:
        # Exit condition - past the end
        # Simple test - pairs of digits eg 11 must be even, triples must be mod-3, etc
        if len(id_str) % match_len != 0:
            return False
        tmp = matcher.findall(id_str)
        if len(tmp) == match_len - 1:
            return True
        match_len += 1

    log.debug(tmp)
    return True


def part_one(input:str) -> int:
    # Convert the array of range strings into numbers. Maybe generators? I can see part 2 being huge spans.
    ranges = parse_ranges(input[0])
    score = 0
    generators = []
    for item in ranges:
        tmp = range(item[0], item[1] + 1)
        generators.append(tmp)

    # Loop over results separately for possible later threading or MP.Pool
    for generator in generators:
        for id in generator:
            if is_invalid(id):
                log.info(f'invalid id {id=} in {generator=}')
                score += id
    return score


def part_two(input: str) -> int:
    # Convert the array of range strings into numbers. Generators are cool.
    ranges = parse_ranges(input[0])
    score = 0
    generators = []
    for item in ranges:
        tmp = range(item[0], item[1] + 1)
        generators.append(tmp)

    # Loop over results separately for possible later threading or MP.Pool
    for generator in generators:
        for id in generator:
            if is_invalid_two(id):
                log.info(f'invalid id {id=} in {generator=}')
                score += id
    return score


def test_part1():
    sample, full, answer, _ = get_all_data(2)
    dut = part_one(sample)
    assert_expr("str(dut) == answer[0]")

    log.info(f'{part_one(full)=}')


def test_part2():
    sample, full, _, answer = get_all_data(2)
    dut = part_two(sample)
    assert_expr('str(dut) == answer[0]')


if __name__ == '__main__':
    test_part1()
    # test_part2()