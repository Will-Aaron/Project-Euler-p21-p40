# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 17:17:34 2022

@author: willi
"""

#Project Euler Problem 26


#As outlined in the following websites "https://mathworld.wolfram.com/MultiplicativeOrder.html" and "https://mathworld.wolfram.com/DecimalPeriod.html"
#The length of the decimal period in the decimal expansion of a unit fraction can be found directly from the multiplicative order of it's denominator
#The multiplicative order of 10 mod an integer n relatively prime to 10 gives the period of the decimal expansion of the reciprocal of n

#Will only have a finite decimal expansion(and thus a cycle of 0) if the rational number is regular, meaning of the form r = p / (2**a * 5**b) where p != 0 mod(2,5)

import math

def multiplicativeOrderTen(n):
    k = 1
    while 10**k%n != 1:
        k += 1
    return k

if __name__ == "__main__":
    d = 1000
    
    dLargest = 3
    maxOrder = 1
    for i in range(2,d):
        if math.gcd(10,i) == 1:
            order = multiplicativeOrderTen(i)
            if order > maxOrder:
                maxOrder = order
                dLargest = i
    print(maxOrder)
    print(dLargest)