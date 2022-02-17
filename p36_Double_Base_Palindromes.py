# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 20:05:59 2022

@author: willi
"""

#Project Euler Problem 36 Double Base Palindromes

def decToBin(n):
    n = int(n)
    return bin(n).replace("0b","")#Using built in binary conversion function with some formatting corrections

def isPalindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

if __name__=="__main__":
    
    limit = 10**6#Limit outlined in challenge
    
    bothPalindrome = []
    
    for i in range(limit):
        if isPalindrome(i):
            if isPalindrome(decToBin(i)):
                bothPalindrome.append(i)
                
    print(sum(bothPalindrome))
    