#!/usr/bin/env python3
import pandas as pd

def part_one():
    sdf = pd.read_csv('data/06s.txt', header=None, delimiter=r'\s+', skipfooter=1).T
    print(sdf.head())
    # Now we need to operators row
    sof = pd.read_csv('data/06s.txt', header=None, delimiter=r'\s+', skiprows=sdf.shape[1]).T
    print(sof.head())

    sdf['oper'] = sof[0]
    sum_score = sdf[sdf.oper == '+'][sdf.columns[:-1]].sum(axis = 1).sum()
    prod_score = sdf[sdf.oper == '*'][sdf.columns[:-1]].prod(axis = 1).sum()
    score = sum_score + prod_score
    print(score)

    sdf = pd.read_csv('data/06.txt', header=None, delimiter=r'\s+', skipfooter=1).T
    print(sdf.head())
    # Now we need to operators row
    sof = pd.read_csv('data/06.txt', header=None, delimiter=r'\s+', skiprows=sdf.shape[1]).T
    print(sof.head())

    sdf['oper'] = sof[0]
    sum_score = sdf[sdf.oper == '+'][sdf.columns[:-1]].sum(axis = 1).sum()
    prod_score = sdf[sdf.oper == '*'][sdf.columns[:-1]].prod(axis = 1).sum()
    score = sum_score + prod_score
    print(score)

if __name__ == '__main__':
    part_one()