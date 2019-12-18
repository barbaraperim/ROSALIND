#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:11:20 2019

@author: Bárbara Perim
"""

def create_punnet_square(first_allele, scnd_allele):
    punnet_square = {}
    for i in range(len(first_allele)):
        for j in scnd_allele:
            new_allele = first_allele[i]+j
            if new_allele in punnet_square:
                punnet_square[new_allele] += 1
            else:
                punnet_square[new_allele] = 1
    return punnet_square
    

def count_dominant_allele(punnet_square):
    count = 0
    for k in punnet_square:
        if k[0].isupper():
            count += 1 * punnet_square[k]
    return count
    
def mendelian_inheritance(no_dominant, no_heterozyguos, no_recessive):
    punnet_dict = {}
    #redudant but better than calling create_punnet at every iteration later
    punnet_dict['XX'] = {'XX': create_punnet_square('XX','XX'),
               'Xx': create_punnet_square('XX','Xx'),
               'xx': create_punnet_square('XX','xx')}
    punnet_dict['Xx'] = {'XX': create_punnet_square('Xx','XX'),
               'Xx': create_punnet_square('Xx','Xx'),
               'xx': create_punnet_square('Xx','xx')}
    punnet_dict['xx'] = {'XX': create_punnet_square('xx','XX'),
               'Xx': create_punnet_square('xx','Xx'),
               'xx': create_punnet_square('xx','xx')}

    
    alelle_list = []
    for i in range(no_dominant):
        alelle_list.append("XX")
    for i in range(no_heterozyguos):
        alelle_list.append("Xx")
    for i in range(no_recessive):
        alelle_list.append("xx")
    print(alelle_list)
    
    total_combinations = 0
    no_dominant_allele = 0
    
    for a in range(len(alelle_list)):
        for b in range(a+1, len(alelle_list)):
            total_combinations +=4
            punnet = punnet_dict[alelle_list[a]][alelle_list[b]]
            no_dominant_allele += count_dominant_allele(punnet)
    print(no_dominant_allele)
    print(total_combinations)
    print(no_dominant_allele/total_combinations)

#print(count_dominant_allele(create_punnet_square("XX","xx")))
mendelian_inheritance(2,2,2)
