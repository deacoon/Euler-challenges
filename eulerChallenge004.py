# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 20:39:58 2017

@author: Deacon
"""

def is_palindrome(text):
    
    half_length = int(len(text)/2)
    head = text[:half_length]
    reversed_tail = "".join(reversed(text))[:half_length]
    
    return head == reversed_tail

def find_largest_palindrome_product(lower_bound, upper_bound):
    
    largest_product = 0
    
    for factor_1 in range(lower_bound, upper_bound):
        for factor_2 in range(factor_1, upper_bound):
            product = factor_1 * factor_2
            if(is_palindrome(str(product))):
                largest_product = max(product, largest_product)
    
    return largest_product

print("solution:", find_largest_palindrome_product(100,1000))