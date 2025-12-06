#!/usr/bin/env python3

import logging
from math import floor

from utils import get_data_lines

logging.basicConfig(level=logging.DEBUG, format='%(pathname)s(%(lineno)s): %(levelname)s %(message)s')
log = logging.getLogger()


def part_one():

    sample_lines, full_lines = get_data_lines(1)

    pos = 50
    zero_count = 0
    for move in full_lines:
        direction = move[0]
        count = int(move[1:])
        log.debug(f'{move=} {direction=} {count=}')
        if direction == 'R':
            pos = (pos + count) % 100
        else:
            pos = (pos - count) % 100
        if pos == 0:
            zero_count += 1
        log.debug(f'{pos=} {zero_count=}')
    log.info(f'part one {zero_count=}')

def two():
    sample_lines, full_lines = get_data_lines(1)

    pos = 50
    zero_count = 0
    for move in full_lines:
        direction = move[0]
        count = int(move[1:])
        log.debug(f'{move=} {direction=} {count=}')
        old_pos = pos
        if direction == 'R':
            pos = pos + count
            low = old_pos
            high = pos
        else:
            pos = pos - count
            low = pos - 1
            high = old_pos - 1

        zero_count_tmp = floor(high / 100) - floor(low / 100)
        zero_count += zero_count_tmp
        log.info(f'{move=} {old_pos=} {pos=} {zero_count_tmp=} {zero_count=}')

    log.info(f'part two {zero_count=}')


if __name__ == "__main__":
    # part_one()
    two()