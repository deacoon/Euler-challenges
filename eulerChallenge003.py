# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:44:11 2017

@author: Deacon
"""


def euler_challenge_003():
    product = 600851475143
       
    return is_prime_divisor(product, 2)


def is_prime(number):

    for divisor in range(2, number):
        if number % divisor != 0:
            return False

    return True


def is_prime_divisor(product, divisor):

    for number in range(divisor+1, product):
        if product % number == 0:
            if is_prime(number):
                return is_prime_divisor(int(product/number), number) 
    return product

    
print("solution:", euler_challenge_003())
