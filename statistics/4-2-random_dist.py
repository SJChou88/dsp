#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:16:01 2017

@author: stephenchou
"""

#Generate 1000 numbers from random.random and plot their PMF and CDF. Is the distribution uniform?

import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot

rsample = np.random.random(1000)

pmf = thinkstats2.Pmf(rsample, label='actual')
thinkplot.Hist(pmf)

#can't see anything meaningful from plot as basically every sample has no duplicates

def EvalCdf(sample, x):
    count = 0.0
    for value in sample:
        if value <= x:
            count += 1

    prob = count / len(sample)
    return prob

cdf = thinkstats2.Cdf(rsample, label='random sample')
thinkplot.Cdf(cdf)

#looks pretty uniform.