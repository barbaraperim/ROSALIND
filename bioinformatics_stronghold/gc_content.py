#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:55:17 2019

@author: Barbara Perim
"""

def gc_count(string):
    g_count = string.count("G")
    c_count = string.count("C")
    return g_count+c_count
def gc_content(gc_count, length):
    return (gc_count/(length))*100

with open("rosalind_gc.txt") as file:  
    highest_gc_content = 0
    highest_gc_content_label = "" 
    label = ""
    line_gc_content = 0
    line_gc_count = 0
    line_len = 0
    for line in file:
        if line[0] == ">":
            if line_gc_content > highest_gc_content:
                highest_gc_content = line_gc_content
                highest_gc_content_label = label
            label = line[1::].strip()
            line_gc_count = 0
            line_gc_content = 0
            line_len = 0
        else:
            line_gc_count += gc_count(line)
            # -1 because of the \n in the end of each line
            # DNA strings were split
            line_len += (len(line)-1)
            if (line_len > 0):
                line_gc_content = gc_content(line_gc_count, line_len)
    if line_gc_content > highest_gc_content:
                highest_gc_content = line_gc_content
                highest_gc_content_label = label
    print(highest_gc_content_label, end=" ")
    print(highest_gc_content)
