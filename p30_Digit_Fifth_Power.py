# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 21:14:38 2022

@author: willi
"""

#Project Euler Problem 30 Digit Fifth Power

#It can be shown by mathematical analysis that the digit m-th power sum of a positive integer is bounded above by
#a maximum of n*9**m for each n digit number. The rate of increase of the maximum is less than the rate of increase of our integers.
#It can be shown by analysis that given the digith m-th power sum function D_m(x),
#For any integer k >= 10**(m+1), k >= D_m(k), therefore we only need to check numbers up to 10**(6)

def digitMPower(x,m = 5): #m Defaults to 5 for this challenge but this can be used for any general m
    #Input number must be an integer or a string with only integers
    x = str(x)
    summation = 0
    for digit in x:
        summation += int(digit)**m
    return summation

if __name__ == "__main__":
    
    m = 5
    sumList = []
    for i in range(2,10**(m+1)):#Disallow 1 as it's not a sum
        if i == digitMPower(i,m):
            sumList.append(i)
    
    print(sumList)
    
    total = sum(sumList)
    print(total)