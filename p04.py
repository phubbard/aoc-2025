#!/usr/bin/env python3
from utils import get_all_data, log, assert_expr, load_2d_arrays, dimensions, print_2d_array

def score_cell(cell: str) -> int:
    if cell == '@':
        return 1
    return 0


def adj_roll_count(inp_data:list, row: int, col: int) -> int:
    # Count of rolls found in the adjacent 8 cells
    num_rows, num_cols = dimensions(inp_data)
    count = 0
    # UL
    if row > 0 and col > 0:
        count += score_cell(inp_data[row - 1][col - 1])
    # Up
    if row > 0:
        count += score_cell(inp_data[row - 1][col])
    # UR
    if row > 0 and col < (num_cols - 1):
        count += score_cell(inp_data[row - 1][col + 1])
    # R
    if col < (num_cols - 1):
        count += score_cell(inp_data[row][col + 1])
    # RD
    if row < (num_rows - 1) and col < (num_cols - 1):
        count += score_cell(inp_data[row + 1][col + 1])
    # D
    if row < (num_rows - 1):
        count += score_cell(inp_data[row + 1][col])
    # DL
    if row < (num_rows - 1) and col > 0:
        count += score_cell(inp_data[row + 1][col - 1])
    # L
    if col > 0:
        count += score_cell(inp_data[row][col - 1])
    return count


def part_one(input_data: list) -> int:
    num_rows, num_cols = dimensions(input_data)
    score = 0
    for current_row in range(num_rows):
        for current_col in range(num_cols):
            if input_data[current_row][current_col] == '.':
                continue
            if adj_roll_count(input_data, current_row, current_col) < 4:
                score += 1
                log.debug(f"x at {current_row=}, {current_col=}")
    log.info(f"{score=}")
    return score


def total_roll_count(input_data: list) -> int:
    num_rows, num_cols = dimensions(input_data)
    score = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if input_data[row][col] == '@':
                score += 1
    return score


def part_two(input_data: list) -> int:
    num_rows, num_cols = dimensions(input_data)
    initial_count = total_roll_count(input_data)

    score = 0
    for current_row in range(num_rows):
        for current_col in range(num_cols):
            if input_data[current_row][current_col] == '.':
                continue
            if adj_roll_count(input_data, current_row, current_col) < 4:
                score += 1
                # Mark it as removed
                input_data[current_row][current_col] = '.'
                log.debug(f"x at {current_row=}, {current_col=}")
    log.info(f"part two {score=}")

    # print_2d_array(input_data)

    while True:
        score = 0
        log.info(f"{total_roll_count(input_data)=}")
        for current_row in range(num_rows):
            for current_col in range(num_cols):
                if input_data[current_row][current_col] == '.':
                    continue
                if adj_roll_count(input_data, current_row, current_col) < 4:
                    score += 1
                    # Mark it as removed
                    input_data[current_row][current_col] = '.'
        log.info(f"part two {score=}")

        if score <= 0:
            break

    return initial_count - total_roll_count(input_data)


def test_part1():
    _, _, s_answer, _ = get_all_data(4)
    sample, full = load_2d_arrays(4)
    score = part_one(sample)
    assert_expr("str(score) == s_answer[0]")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    log.info(f'{part_one(full)=}')


def test_part2():
    _, _, _, answer = get_all_data(4)
    sample, full = load_2d_arrays(4)
    score = part_two(sample)
    assert_expr("str(score) == answer[0]")
    log.info("** Doing full dataset **")
    # if we got here, we can proceed to the full data set
    log.info(f'{part_two(full)=}')


if __name__ == '__main__':
    # test_part1()
    test_part2()