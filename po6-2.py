#!/usr/bin/env python3

from utils import get_all_data, log, assert_expr, get_column, make_2d_array, dimensions, product, Data2D


def part_two_classy(sample: bool) -> int:
    # Solve using the new class
    data = Data2D()
    data.load(6, sample=sample, strip=False, fill=' ')

    num_rows, num_cols = data.dimensions()
    ops_row = data[num_rows - 1]
    ops = [x for x in ops_row if x.strip()]

    # find the empty columns
    blank_cols = []
    for idx in range(len(data[0])):
        col = data.column(idx)
        if all([x.isspace() for x in col]):
            blank_cols.append(idx)
    # To use the pop operator, we need a pseudo-blank column at the end
    blank_cols.append(num_cols)

    # Now we iterate, using the blank columns as starting and ending points.
    last_col = 0
    score = 0
    for cur_op in ops:
        start_col = last_col
        end_col = blank_cols.pop(0)
        col_vals = []
        for idx in range(start_col, end_col):
            col = data.column(idx)
            # drop the last item - operator row
            col.pop()
            # Smush it into an integer
            col_vals.append(int(''.join(col)))
        if cur_op == '*':
            col_score = product(col_vals)
        else:
            col_score = sum(col_vals)
        score += col_score
        last_col = end_col + 1

    log.info(f"{sample=} {score=}")
    return score


def part_two(sample: bool) -> int:
    ops, data, blank_cols = load_data(sample=sample)
    last_col = 0
    score = 0
    num_rows, num_cols = dimensions(data)
    # To use the pop operator, we need a pseudo-blank column at the end
    blank_cols.append(num_cols)

    for cur_op in ops:
        start_col = last_col
        end_col = blank_cols.pop(0)
        col_vals = []
        for idx in range(start_col, end_col):
            col = get_column(data, idx)
            col_vals.append(int(''.join(col)))
        if cur_op == '*':
            col_score = product(col_vals)
        else:
            col_score = sum(col_vals)
        score += col_score
        last_col = end_col + 1

    return score


def load_data(sample=True, problem_number=6):
    # Odd data equals custom loader
    zero_padded = f"{problem_number:02}"
    sample_file = f'./data/{zero_padded}s.txt'
    data_file = f'./data/{zero_padded}.txt'

    if sample:
        input_data = open(sample_file, 'r').readlines()
    else:
        input_data = open(data_file, 'r').readlines()

    # Extract the operators
    ops_row = input_data[len(input_data) - 1]
    ops = ops_row.split()
    # We have an array of strings - want a 2d array of characters
    data = make_2d_array(len(input_data), len(input_data[0]), fill=' ')

    for cur_row_idx, cur_row in enumerate(input_data):
        if cur_row_idx == len(input_data) - 1:
            continue

        for cur_char_idx, cur_char in enumerate(cur_row):
            if cur_char == '\n':
                continue
            data[cur_row_idx][cur_char_idx] = cur_char

    # find the empty columns
    blank_cols = []
    for idx in range(len(data[0])):
        col = get_column(data, idx)
        if all([x.isspace() for x in col]):
            blank_cols.append(idx)

    log.debug(f"{blank_cols=}")

    return ops, data, blank_cols


def part_one(input_data: list) -> int:
    ops_row = input_data[len(input_data) - 1]
    ops = ops_row.split()

    data = []
    for x in range(len(input_data) - 1):
        data.append(input_data[x].split())

    score = 0
    for idx in range(len(ops)):
        col_str = get_column(data, idx)
        col = [int(x) for x in col_str]
        if ops[idx] == '*':
            col_score = product(col)
        else:
            col_score = sum(col)
        score += col_score
    return score


def test_part1():
    sample, full, answer, _ = get_all_data(6)
    score = part_one(sample)
    assert_expr("str(score) == answer[0]")
    log.info("Doing full part 1 dataset")
    # if we got here, we can proceed to the full data set
    log.info(f'{part_one(full)=}')


def test_part2():
    score = part_two(sample=True)
    _, _, p1a, p2a = get_all_data(6)
    assert_expr("str(score) == p2a[0]")

    log.info("Doing full part 2 dataset")
    # if we got here, we can proceed to the full data set
    score = part_two(sample=False)
    log.info(f'{score=}')


if __name__ == '__main__':
    test_part1()
    test_part2()
    part_two_classy(True)
    part_two_classy(False)