#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:05:03 2019

@author: Bárbara Perim
"""

def rabbits(months, n_pairs):
    if (months < 1):
        return 0
    if (months == 1):
        return 1
    else:
        return rabbits(months-1, n_pairs) + n_pairs * rabbits(months-2, n_pairs)

print(rabbits(34,4))
