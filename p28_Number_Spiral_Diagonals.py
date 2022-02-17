# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 20:07:19 2022

@author: willi
"""

#Project Euler Problem 28 Number Spiral Diagonals

#Summation can be proven by induction on an index k for the sum of the four diagonals on a 2*k+1 grid at each level.
#A k+1 level's corner values are spaced by 2*k+2 from the previous k level's corner,
#while the top right corner of the k+1 level is solved by (2*k+1)**2,
#thereby for any level k we can solve for the sum of the four corners of the k+1 level. Simpler to just have computer calculate the rest of the sum rather than solve the last step by mathematical induction

if __name__ == "__main__":
    summation = 1
    for k in range(500):
        summation += 4*((2*k+1)**2) + 20*(k+1)
    
    print(summation)