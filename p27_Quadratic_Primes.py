# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 18:50:10 2022

@author: willi
"""

#Project Euler Problem 27 Quadratic Primes


#General quadratic formula Q(n) = n**2 + a*n + b, must produce primes for 0 <= n <= c, for some c. Want to find a,b such c is maximum
#Since our goal is to find a,b which maximize c, we can demand certain conditions which increase c and limit cases of checks to make for a and b

#Primes must be positive, therefore demand Q(n) > 0 for choice values of n, such that it might be prime
#If n=0, then Q(0) = b > 0, and in fact b must be a prime as well. Although we don't need to check to reduced cases because the process of checking each primality of b would be the same as checking n=0 validity
#If n=1, then Q(1) = 1+a+b, therefore b > -(a+1). Which creates a high lower bound for b provided that a is negative
#These conditions must be true if n=0 or n=1 is able to be prime. Note that they do not imply that Q(0) or Q(1) are prime.

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

def maxQuadratic(a,b):
    n = 0
    while isPrime(n**2 + a*n + b):
        n +=1
    n -= 1
    
    if n == -1:
        return None
    else:
        return n

if __name__ == "__main__":
    print(isPrime(41))
    print(maxQuadratic(-79, 1601))
    
    aLimit = 1000
    bLimit = 1000
    maxA = 0
    maxB = 0
    maxC = 0
    
    for a in range(-(aLimit-1),(aLimit-1)):
        for b in range(max(0,-(a+1)),bLimit):
            c = maxQuadratic(a, b)
            if c != None:
                if c > maxC:
                    maxA = a
                    maxB = b
                    maxC = c
                
    print("a: {}".format(maxA))
    print("b: {}".format(maxB))
    print("c: {}".format(maxC))
    print("Product: {}".format(maxA*maxB))