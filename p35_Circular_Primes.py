# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 17:14:38 2022

@author: willi
"""

#Project Euler Problem 35 Circular Primes

def isPrime(n): #Using 6k+-1 optimization "https://en.wikipedia.org/wiki/Primality_test"
    if n <=3:#If the number is 2 or three then prime, so check with conditional for greater than 1
        return n > 1
    if n %2 == 0 or n%3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % (i) == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def cycleNum(n):
    
    n = str(n)
    cycles = []
    
    for i in range(len(n)):
        cycles.append(int(n))
        n = n[1:] + n[:1]
    return cycles

#Can quickly disregard a possible number if we see that it contains an even digit, because then it's cycle will result in an even and therefore non prime number
def containsEven(n):
    n = str(n)
    for digit in n:
        if int(digit)%2 == 0:
            return True
    return False

if __name__=="__main__":
    
    limit = 10**6#Limit for challenge is one million
    
    
    countCirc = 1 #Initialize knowing that 2 is a circular prime then continuing on from there
    circular = [2] #Records Circular Primes, not necessary for challenge
    
    for i in range(3,limit):
        #First check for even number to disregard it
        if not containsEven(i):
            cycles = cycleNum(i)
            isCir = True
            #Assume it is a circular prime to being with, then iterate over cycles and if you find a counter example of a non prime number, then change isCir to false and fail to increment
            for num in cycles:
                if not isPrime(num):
                    isCir = False
                    break
            if isCir:
                countCirc += 1
                #circular.append(i) #For recording circular primes, not necessary for challenge
                
    print(countCirc)
    