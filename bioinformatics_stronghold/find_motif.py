#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 01:11:32 2019

@author: Bárbara Perim
"""

with open("rosalind_subs.txt") as f:
    data = f.readlines()
    dna_string = data[0].rstrip()
    dna_substring = data[1].rstrip()
    
    index = dna_string.find(dna_substring, 0)
    
    with open ("output.txt", "w") as f_w:        
        while(index != -1):
            f_w.write(str(index+1) + " ")
            index = dna_string.find(dna_substring, index+1)