# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:51:56 2017

@author: Deacon
"""


def smallest_multiple(lower_bound, upper_bound):
    
    multiple = upper_bound
    while True:
        found_multiple = True
        for number in range(lower_bound, upper_bound):
            if multiple % number != 0:
                found_multiple = False
                break
        
        if found_multiple:
            return multiple
        
        multiple += upper_bound
        
    
print("solution:", smallest_multiple(1, 20))
