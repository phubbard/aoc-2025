#!/usr/bin/env python3
from utils import get_all_data, log, assert_expr


def parse_ranges(input: str) -> list:
    # Parse '11-22,95-115' into [[11, 22], [95-115]]
    ranges = input.split(',')
    rc = []
    max_rangeval = -1
    for item in ranges:
        tmp = item.split('-')
        lvalue = int(tmp[0])
        rvalue = int(tmp[1])
        mv = max(lvalue, rvalue)
        max_rangeval = max(max_rangeval, mv)
        rc.append([lvalue, rvalue])

    log.debug(f'{len(rc)=}')
    log.info(f"{max_rangeval=} {len(str(max_rangeval))=} digits")
    return rc


def is_invalid(id: int) -> bool:
    # Part 1 - pairwise digit comparison, simple and fast
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


def part_one(input: str) -> int:
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


def generate_repeats(kernel, max_len=10) -> list:
    rc = []
    for k in range(2, max_len + 1):
        candidate = str(kernel) * k
        if len(candidate) <= max_len:
            rc.append(candidate)

    return rc


def part_two(input: str) -> int:
    # Convert the array of range strings into numbers.
    str_ranges = parse_ranges(input[0])
    score = 0
    input_ranges = []
    for item in str_ranges:
        input_ranges.append((item[0], item[1] + 1))

    iveseenit = []
    all_num_strs = [str(x) for x in range(1, 100_000)]
    for kernel in all_num_strs:
        if kernel not in iveseenit:
            search_list = generate_repeats(kernel)
            iveseenit.extend(search_list)
            for item in search_list:
                item_value = int(item)
                for cur_list in input_ranges:
                    if item_value in range(cur_list[0], cur_list[1]):
                        score += item_value
        else:
            log.info(f"{score=} {kernel=}")

    log.info(f"final {score=}")

    return score


def test_part1():
    sample, full, answer, _ = get_all_data(2)
    dut = part_one(sample)
    assert_expr("str(dut) == answer[0]")

    log.info(f'{part_one(full)=}')


def test_part2():
    sample, full, _, answer = get_all_data(2)
    dut = part_two(full)
    # assert_expr('str(dut) == answer[0]')


if __name__ == '__main__':
    # test_part1()
    test_part2()
