# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:24:34 2022

@author: willi
"""

#Project Euler Problem 21

def divisorSum(n):
    
    if n==1:
        return 0
    divisorSum = 1
    #Number is a proper divisor if it's modular remainder is zero. A proper divisor is strictly less than the number,
    #so we would only need to test numbers up to half of the input number.
    for i in range(2,n//2 + 1):
        if n%i == 0:
            divisorSum += i
    return divisorSum

def compareDivSum(array):
    totalSum = 0
    for j in range(len(array)):
        if j+1 != array[j] and array[j] <= len(array):#This ensures we aren't choosing perfect numbers and that we are choosing a number with a divisor sum that's less than our size for comparison
            if j+1 == array[array[j]-1]:
                #This conditions satisfies requirements for a pair of amicable numbers
                totalSum += j+1 + array[j]
                #With this setup, each pair of amicable numbers will be found twice, as we are iterating over every number, so divide final result by 2
                
    return totalSum//2

if __name__=="__main__":
    size = 9999 #Check all numbers up to size
    
    divSum = [0] * size #Allocates array to place divisor numbers inside
    
    for k in range(size):
        divSum[k] = divisorSum(k+1)
    
    #print(divSum)
    print(compareDivSum(divSum))
    #Now all divisor sums up to size are located in the array
    
    