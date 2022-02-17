# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 21:34:15 2022

@author: willi
"""

#Project Euler Problem 31 Coin Sums

#Step Process which builds number of solutions by counting possible ways with amounts from 0 to endSum with smaller denominations,
#Then incrementing up denominations to count possibilities from 0 to endSum again, until finall considering all possible denominations


if __name__=="__main__":
   
    #Outlines choice of coins and target sum
    coins = [1,2,5,10,20,50,100,200]
    endSum = 200
    
    
    
    #Forms count array
    count = [0] * (endSum+1) #In challenge, will have 201 slots for ways to make change for 0p to 200
    
    count[0] = 1 #We define this as 1 way for recursive purposes, because we know that if we are counting the ways of making
    # say 2p with just 2p coins, we know that however many ways 0p can be create will calculate it for us, we just need to take each one of those ways and incude a 2p coin
    
    #print("Initial: {}".format(count))
    
    for denom in coins:
        for target in range(denom,len(count)):
            #print("Denom: {} Target: {}".format(denom,target))
            previousWays = count[target-denom]
            #print("Previous Ways: {}".format(previousWays))
            count[target] += previousWays
            #print("Count: {}".format(count))
            
    print("Sum Total: {} Ways to produce endSum: {} with coins {}".format(count[endSum],endSum,coins))
    