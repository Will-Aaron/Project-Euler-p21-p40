# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 12:49:46 2022

@author: willi
"""

#Project Euler Problem 38 Pandigital multiples

def isNPandigital(num,n = 9): #Defaults to 9 for challenge
    num = str(num)
    #Easy check, must only have n characters to be pandigital through 1 to n
    if len(num) != n:
        return False
    #After this point then the string must have characters which are digits 1 through n, so if it's not an integer or is less than 1 or greater than n,
    #then there is not enough space and it fails the pandigital check
    
    usedDigit = []
    for digit in num:
        try:
            int(digit)
        except ValueError:
            return False
        
        if int(digit)< 1 or int(digit) > n:
            return False
        elif digit in usedDigit:
            return False
        else:
            usedDigit.append(digit)
    return True
    
if __name__=="__main__":
    
    maxPandigital = 123456789 #Initialize maximum as lowest 9 digit pandigital number so that and larger ones are found and replace it
    
    kLimit = 10**4 #It can be shown by the n>1 tuple constraint that for any integer greater than this limit, the use of the smallest tuple (1,2) produces at least a 10 digit number, thereby going beyond the scope of challenge
    for k in range(1,kLimit):
        
        product = str(k)+str(k*2) #All products must have concatenation with multiplication by 1 and 2 at least
        i = 3
        while len(product) < 9:
            product += str(k*i)
            i += 1
        
        #Must have exactly a 9 digit number and is pandigital, which is tested in the isPandigital function
        if isNPandigital(product):
            product = int(product)
            if maxPandigital < product:
                maxPandigital = product
                
    print(maxPandigital)