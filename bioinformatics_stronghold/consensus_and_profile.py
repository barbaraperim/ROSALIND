#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:56:18 2019

@author: Bárbara Perim
"""

def create_profile(dna_strings):
    #we must be sure they all have the same length
    n_list = [0 for i in range(len(dna_strings[0]))]
    profile = {"A":n_list.copy(),"C":n_list.copy(),"G":n_list.copy(),"T":n_list.copy()}
    for string in dna_strings:
        for n in range(len(string)):
            profile[string[n]][n]+=1
    return profile

def create_consensus(profile):
    consensus = ['X' for i in range(len(profile['A']))]
    for i in range(len(consensus)):
        max = 'A'
        for key in profile:
            if profile[key][i] >= profile[max][i]:
                max = key
        consensus[i]=max
    return consensus
            
with open("rosalind_cons.txt") as f_r:
    with open ("output.txt", "w") as f_w:    
        line = f_r.readline().rstrip()
        dna_strings = []
        index = -1
        while line:
            if line[0] == ">":
                index+=1
            else:
                if len(dna_strings) > index:
                    dna_strings[index] += line
                else:
                    dna_strings.append(line)
            
            line = f_r.readline().rstrip()
        
        profile = create_profile(dna_strings)
        consensus = create_consensus(profile)
        
        f_w.write("".join(consensus))
        f_w.write("\n")
        for key in profile:
            f_w.write(key + ":")
            for i in profile[key]:
                f_w.write(" " + str(i))
            f_w.write("\n")