#!/usr/bin/env python3
from utils import get_all_data, log, assert_expr
from math import sqrt
import numpy as np


def parse(input_data: list) -> list:
    rc = []
    for line in input_data:
        values = line.split(',')
        tmp = (int(values[0]), int(values[1]), int(values[2]))
        rc.append(tmp)

    return rc


def distance(a: tuple, b: tuple) -> float:
    diffs = [a[x] - b[x] for x in range(3)]
    dsquared = [x * x for x in diffs]
    dist = sqrt(sum(dsquared))
    return dist


def same(a: tuple, b: tuple) -> bool:
    return all([a[x] == b[x] for x in range(3)])


def in_circ(pt: tuple, circuit: list) -> bool:
    for point in circuit:
        if same(pt, point):
            return True
    return False


def find_closest(a: tuple, distances: list) -> tuple:
    connected = []
    for dist in distances:
        if same(dist[0], a):
            if not same(a, dist[1]):
                connected.append(dist)

    closest_pt = min(connected, key=lambda x: x[2])
    print('closest is ', a, closest_pt)
    return closest_pt


def find_all_pairs(data: list) -> list:
    # Data struct is tuple of (a, b, distance)
    log.info(f"computing all-pairs for {len(data)=}")
    distances = []
    for a_idx, a in enumerate(data):
        for b_idx, b in enumerate(data):
            distances.append((a, b, distance(a, b)))
    log.info(f"Done, {len(distances)=}")
    return distances


def part_one(input_data: list, num_pairs=10) -> int:
    data = parse(input_data)
    # print(distance(data[0], data[1]))
    distances = find_all_pairs(data)
    first_chunk = [x for x in distances if x[2] > 0]
    first_chunk.sort(key=lambda x: x[2])
    trimmed_chunk = first_chunk[:num_pairs * 2]
    unique_nodes = set([x[0] for x in trimmed_chunk])
    circuits = [[x] for x in unique_nodes]

    for connection in trimmed_chunk:
        disjoint = []
        newcirc = []

        for c in circuits:
            if in_circ(connection[0],c):
                newcirc.extend(c)
            elif in_circ(connection[1],c):
                newcirc.extend(c)
            else:
                disjoint.append(c)
        circuits = disjoint + [newcirc]

    circuits.sort(key = lambda x:len(x), reverse=True)

    return (len(circuits[0]) * len(circuits[1]) * len(circuits[2]))


def part_two(input_data: list) -> int:
    return 0


def test_part1():
    sample, full, answer, _ = get_all_data(8)
    score = part_one(sample, num_pairs=10)
    # assert_expr("str(score) == answer[0]")
    log.info(f"part one sample {score=}")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    score = part_one(full, num_pairs=1000)
    log.info(f'part one full dataset {score=}')


def test_part2():
    sample, full, _, answer = get_all_data(8)

    score = part_two(sample)
    assert_expr("str(score) == answer[0]")
    log.info("Doing full dataset")
    # if we got here, we can proceed to the full data set
    log.info(f'{score=}')


if __name__ == '__main__':
    test_part1()
    # test_part2()