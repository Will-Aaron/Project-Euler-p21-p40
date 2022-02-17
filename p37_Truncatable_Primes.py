# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:59:32 2022

@author: willi
"""

#Project Euler Problem 38 Truncatable Primes

#Challenge does not consider 2,3,5,7 to be truncatable primes. However this code considers them to be truncatable primes
#to produce more truncatable primes. Remove contribution at end

def isPrime(n): #Using 6k+-1 optimization "https://en.wikipedia.org/wiki/Primality_test"
    n = int(n)
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

def produceLeftTruncated(array, n): #Note that producing the set of Left Truncated Primes is computationally expensive and not completely neccessary for challenge
        #Operates under assumption that input is truncatable prime, produces truncatable primes which truncate to input, and includes them into collection array
        n = str(n)
        for digit in ["1","2","3","4","5","6","7","8","9"]:
            create = int(digit+n)
            if isPrime(create):
                array.append(create) #Appends to array without returning, ensure array is in global scope

def produceRightTruncated(array, n):
        #Operates under assumption that input is truncatable prime, produces truncatable primes which truncate to input, and includes them into collection array
        n = str(n)
        for digit in ["1","2","3","4","5","6","7","8","9"]:
            create = int(n+digit)
            if isPrime(create):
                array.append(create) #Appends to array without returning, ensure array is in global scope
                
def isLeftTruncated(n):#Tests if the provided number is a leftTruncatable Prime
    n = int(n)
    while isPrime(n):
        n = str(n)
        n = n[1:] #Removes leftmost digit
        if n == "": #If n is the empty string, meaning all left slices were prime and the empty string is all that remains, then it's true
            return True
        n = int(n)
    return False

def isRightTruncated(n):#Tests if the provided number is a rightTruncatable Prime. Not needed in challenge
    n = int(n)
    while isPrime(n):
        n = str(n)
        n = n[:-1] #Removes rightmost digit
        if n == "": #If n is the empty string, meaning all left slices were prime and the empty string is all that remains, then it's true
            return True
        n = int(n)
    return False
            

if __name__=="__main__":
    
    leftRightTruncated = []
    rightTruncated = [2,3,5,7]
    
    for num in rightTruncated:
        produceRightTruncated(rightTruncated, num)
    
    for num in rightTruncated:
        if isLeftTruncated(num):
            leftRightTruncated.append(num)
    
    sumTotal = sum(leftRightTruncated) - 2 - 3 - 5 - 7
    print(sumTotal)