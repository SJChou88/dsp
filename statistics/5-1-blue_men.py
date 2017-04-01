#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:32:14 2017

@author: stephenchou
"""

import numpy as np

import nsfg
import first
import analytic

import thinkstats2
import thinkplot

import scipy.stats


mu = 178
sigma = 7.7

lowerlimit = 177.8 # 5'10
upperlimit = 185.42 # 6'1
dist = scipy.stats.norm(loc=mu, scale=sigma)
dist.cdf(mu-sigma)

upper = scipy.stats.norm.cdf(upperlimit, loc = mu, scale = sigma)
lower = scipy.stats.norm.cdf(lowerlimit, loc = mu, scale = sigma)
bmg_range = upper - lower
print(bmg_range)