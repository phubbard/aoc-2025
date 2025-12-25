#!/usr/bin/env python3
from utils import get_all_data, log, assert_expr
import numpy as np

def bfi_highest_two(bank: str) -> int:
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


def helper(ad,cur_num_left_to_find):
    #cur_num_left_to_find how many digits we must find after finding the current digit.
    simplify = ad[:len(ad)-cur_num_left_to_find]
    digis, firstlocs, couns = np.unique(simplify, return_index=True, return_counts=True, sorted=True)
    best_digit = digis[-1]
    best_loc = firstlocs[-1]
    return best_digit, ad[best_loc+1:]


def find_joltage(bank, num_batteries):
    jlist = []
    newbank = [x for x in bank]
    for i in range(num_batteries-1, -1, -1):
        bd, newbank = helper(newbank,i)
        jlist.append(bd)

    rc = int(''.join(jlist))
    log.debug(f'joltage={rc}')

    return rc


def test_part1():
    sample, full, answer, _ = get_all_data(3)
    dut = part_one(sample)
    assert_expr("str(dut) == answer[0]")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    log.info(f'{part_one(full)=}')


def test_part2():
    sample, full, _, answer = get_all_data(3)

    score = 0
    for bank in sample:
        score += int(find_joltage(bank, 12))
    log.info(f'{score=}')
    # dut = part_two(sample)
    assert_expr("str(score) == answer[0]")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    score = 0
    for bank in full:
        score += int(find_joltage(bank, 12))
    log.info(f'{score=}')


if __name__ == '__main__':
    test_part1()
    test_part2()