# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 13:00:25 2022

@author: willi
"""

#Project Euler Problem #32 Pandigital Products



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
    
    n = 9
    aLim = 98
    bLim = 9876
    
    products = []
    
    for a in range(2,aLim):
        
        for b in range(a+1,bLim):
            c = a * b
            #Intigate check to break out of for loop if the resulting product generates
            panString = str(a)+str(b)+str(c)
            if len(panString) > n:
                break
            if isNPandigital(panString,n):
                if c not in products:
                    products.append(c)
                    
    print(sum(products))
                