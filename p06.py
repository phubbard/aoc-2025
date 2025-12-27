#!/usr/bin/env python3
import pandas as pd
import numpy as np



def part_one():
    sdf = pd.read_csv('data/06s.txt', header=None, delimiter=r'\s+', skipfooter=1).T
    print(sdf.head())
    # Now we need to operators row
    sof = pd.read_csv('data/06s.txt', header=None, delimiter=r'\s+', skiprows=sdf.shape[1]).T
    print(sof.head())

    sdf['oper'] = sof[0]
    sum_score = sdf[sdf.oper == '+'][sdf.columns[:-1]].sum(axis=1).sum()
    prod_score = sdf[sdf.oper == '*'][sdf.columns[:-1]].prod(axis=1).sum()
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


def part_two():
    ###
    # Sample Data
    ###
    #Get the data which will be as strings
    xdf = pd.read_csv('data/06s.txt', header=None, skipfooter=1)
    #Turn said strings into an array
    pinf = xdf.values.flatten()
    #For the sample data we need to add spaces at the end.  This is not necessary for the regular data.
    pinf[0] = pinf[0] + ' '
    pinf[1] = pinf[1] + ' '
    #Split the strings into individual components, which creates a 2d array
    garg = np.array([list(x) for x in pinf])
    print(garg)
    #To do this the cephlapod way we must join the strings going down into single strings
    pick = np.apply_along_axis(lambda x: ''.join(x), 0, garg)
    print(pick)
    #Remove the spacers, return into ints, and reshape into the correct number of rows.  We are not even pretending
    #that we are making this generalizable.
    ceph = np.array([int(x) for x in pick if x != '   ']).reshape((-1,3))
    print(ceph)

    sdf = pd.DataFrame(ceph)
    print(sdf.head)
    sof = pd.read_csv('data/06s.txt', header=None, delimiter=r'\s+', skiprows=sdf.shape[1]).T
    print(sof.head())
    sdf['oper'] = sof[0]
    sum_score = sdf[sdf.oper == '+'][sdf.columns[:-1]].sum(axis = 1).sum()
    prod_score = sdf[sdf.oper == '*'][sdf.columns[:-1]].prod(axis = 1).sum()
    score = sum_score + prod_score
    print(score)

    ###
    # Full Data
    ###
    #Get the data which will be as strings
    xdf = pd.read_csv('data/06.txt', header=None, skipfooter=1)
    #Turn said strings into an array
    pinf = xdf.values.flatten()
    #Split the strings into individual components, which creates a 2d array
    garg = np.array([list(x) for x in pinf])
    print(garg)
    #To do this the cephlapod way we must join the strings going down into single strings
    pick = np.apply_along_axis(lambda x: ''.join(x), 0, garg)
    print(pick)
    #So, because we don't have consistent lengths of the numbers, we can't use reshape like we did for the sample.
    #Deviating sideways
    #
    #Creating arrays to which we will need to apply each operator
    sub_pick = np.array_split(pick,np.where(pick=='    ')[0])
    #And then because each of these has the '   ' at the start except the first...
    hysup = [sub_pick[0]] + [x[1:] for x in sub_pick[1:]]
    #Converting to ints
    ceph = [x.astype('int') for x in hysup]

    sdf = pd.DataFrame(ceph) #And this will had NaN's where ever there are blanks... So hopefully this works.  Fingers crossed.
    print(sdf.head())
    sof = pd.read_csv('data/06.txt', header=None, delimiter=r'\s+', skiprows=sdf.shape[1]).T
    print(sof.head())
    sdf['oper'] = sof[0]
    sum_score = sdf[sdf.oper == '+'][sdf.columns[:-1]].sum(axis = 1).sum()
    prod_score = sdf[sdf.oper == '*'][sdf.columns[:-1]].prod(axis = 1).sum()
    score = sum_score + prod_score
    print(score)





if __name__ == '__main__':
    part_one()