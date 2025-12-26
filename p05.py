#!/usr/bin/env python3
from utils import get_all_data, log, assert_expr


def parse_data(inp_data: list) -> tuple:
    ranges = []
    ingredients = []
    in_ingredients = False
    for line in inp_data:
        if len(line) == 0:
            in_ingredients = True
            continue
        if in_ingredients:
            ingredients.append(int(line))
        else:
            tmp = line.split('-')
            ranges.append((int(tmp[0]), int(tmp[1])))

    return ranges, ingredients


def in_range(ingr: int, irange: tuple) -> int:
    if irange[0] <= ingr <= irange[1]:
        return 1
    return 0


def part_one(fresh_ranges: list, ingredient_ids: list) -> int:
    score = 0
    for ingr in ingredient_ids:
        rcs = [in_range(ingr, x) for x in fresh_ranges]
        score += any(rcs)

    return score


def part_two(start_ranges: list) -> int:
    fresh_ranges = [x for x in start_ranges]
    fresh_ranges.sort(key=lambda x: x[0])

    final_fresh = []
    while(len(fresh_ranges)> 1):

        bp = 0
        #Find the break index for sets that overlap the first set and those that don't
        for i in range(1,len(fresh_ranges)):
            if fresh_ranges[i][0] <= fresh_ranges[0][1]:
                bp = i
        #If there are no sets overlapping the first set, save the first set aside and then loop over remaining list
        if bp == 0:
            final_fresh.append(fresh_ranges[0])
            fresh_ranges = fresh_ranges[1:]
        #Take all of the overlapping sets (i.e. the first bp+1 things on the list) and merge into one set.
        #Replace the overlapping sets with the one set on the list and then send back to loop.
        else:
            new_start = (fresh_ranges[0][0],max([fresh_ranges[i][1] for i in range(bp+1)]))
            fresh_ranges = [new_start]+fresh_ranges[bp+1:]
    final_fresh.extend(fresh_ranges)

    score = 0
    for cur_range in final_fresh:
        score += (cur_range[1] - cur_range[0]) + 1
    log.info(f"{final_fresh=}")
    return score


def test_part1():
    sample, full, answer, _ = get_all_data(5)
    # Split data into fresh ranges and ingredients
    fresh_ranges, ingredient_ids = parse_data(sample)
    score = part_one(fresh_ranges, ingredient_ids)
    assert_expr("str(score) == answer[0]")
    log.info("** Doing full dataset **")
    # if we got here, we can proceed to the full data set
    fresh_ranges, ingredient_ids = parse_data(full)
    log.info(f'{part_one(fresh_ranges, ingredient_ids)=}')


def test_part2():
    sample, full, _, answer = get_all_data(5)
    fresh_ranges, _ = parse_data(sample)
    score = part_two(fresh_ranges)
    assert_expr("str(score) == answer[0]")
    log.info("** Doing full dataset **")
    # if we got here, we can proceed to the full data set
    log.info(f'{score=}')
    fresh_ranges, _ = parse_data(full)
    score = part_two(fresh_ranges)
    log.info(f'full {score=}')


if __name__ == '__main__':
    test_part1()
    test_part2()