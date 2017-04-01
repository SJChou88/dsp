#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:02:14 2017

@author: stephenchou
"""

from __future__ import print_function, division

import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot

resp = nsfg.ReadFemResp()
d = resp.numkdhh
hist = thinkstats2.Hist(d, label='kids')



pmf = thinkstats2.Pmf(d, label='actual')

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

biased_pmf = BiasPmf(pmf, label='observed')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Config(xlabel='Family size', ylabel='PMF')

print('Actual mean', pmf.Mean())
print('Observed mean', biased_pmf.Mean())