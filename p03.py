#!/usr/bin/env python3
from utils import get_all_data, log, assert_expr


def find_max(bank: str, start_idx: int) -> tuple:
    if start_idx >= len(bank):
        return '0','0'

    for k in '987654321':
        k_idx = bank.find(k, start_idx)
        if k_idx >= 0:
            return k, k_idx


def part_one(data) -> int:
    max_joltage = 0
    score = 0
    for bank in data:
        left_digit, index = find_max(bank, 0)
        right_digit, _ = find_max(bank, index+1)
        max_joltage = int(left_digit + right_digit)
        score += max_joltage
        log.info(f"{bank=} {max_joltage} {score=}")

    return score


def test_part1():
    sample, full, answer, _ = get_all_data(3)
    dut = part_one(sample)
    assert_expr("str(dut) == answer[0]")

    # log.info(f'{part_one(full)=}')


if __name__ == '__main__':
    test_part1()