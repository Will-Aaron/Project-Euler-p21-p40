# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 19:51:48 2022

@author: willi
"""

#Project Euler Problem 29 Distinct Powers

if __name__ == "__main__":
    
    aLimit = 100#Is 100 for Challenge
    bLimit = 100#Is 100 for Challenge
    
    powersSet = set()
    for a in range(2,aLimit+1):
        for b in range(2,bLimit+1):
            powersSet.add(a**b)
    
    print(len(powersSet))