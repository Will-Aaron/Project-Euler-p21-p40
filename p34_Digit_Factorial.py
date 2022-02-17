# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 17:07:25 2022

@author: willi
"""

#Project Euler Problem 34 Digit Factorial

#Similarly to Problem 30, we can deomstrate a bound in which an integer is definitivly greater than it's digit factorial sum.
#It can be shown by analysis that an upper limit of 10**7 is enough, and any integers above that will have a factorial digit sum which is less than itself

import math

def digitFac(x):
    x = str(x)
    summation = 0
    for digit in x:
        summation  += math.factorial(int(digit))
    return summation

if __name__=="__main__":
    
    limit = 10**7
    
    sumList = []
    
    for i in range(3,limit):
        if i == digitFac(i):
            sumList.append(i)
    print(sumList)
    print(sum(sumList))
    