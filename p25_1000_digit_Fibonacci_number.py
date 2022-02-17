# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 15:46:17 2022

@author: willi
"""

#Project Euler Problem 25 1000-Digit Fibonacci number

def nextFibonnaci():
    a = 0
    b = 0
    while True:
        F = a + b
        if F == 0:
            F = 1
        yield F
        b = a
        a = F

if __name__=="__main__":
    
    index = 1
    for num in  nextFibonnaci():
        if len(str(num)) == 1000:
            #print(num)
            break
        index += 1
        #print(num)
    print("Final Number is {}th Fibonacci Number.".format(index))