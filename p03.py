#!/usr/bin/env python3
from utils import get_all_data, log, assert_expr


def bfi_highest_two(bank: str) -> int:
    first_digit = second_digit = None
    best_score = 0
    for cur_idx, cur_batt in enumerate(bank):
        for sec_idx, sec_batt in enumerate(bank[cur_idx + 1:]):
            candidate = int(cur_batt + sec_batt)
            best_score = max(best_score, candidate)
    return best_score


def part_one(data) -> int:
    score = 0
    for bank in data:
        max_joltage = bfi_highest_two(bank)
        score += max_joltage
        log.debug(f"{bank=} {max_joltage} {score=}")
    return score


def part_two(data) -> int:
    return 0


def test_part1():
    sample, full, answer, _ = get_all_data(3)
    dut = part_one(sample)
    assert_expr("str(dut) == answer[0]")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    log.info(f'{part_one(full)=}')


def test_part2():
    sample, full, _, answer = get_all_data(3)
    dut = part_two(sample)
    assert_expr("str(dut) == answer[0]")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    log.info(f'{part_two(full)=}')


if __name__ == '__main__':
    test_part1()
    test_part2()