# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:53:21 2022

@author: willi
"""

#Project Euler P23 Non-abundant sums

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


if __name__ == "__main__":
    
    limit = 28123 #Proven to be 28123 by analysis
    #Generate List of abundant Numbers, will only need to check\define abundant numbers up to the limit, as we will only check possible numbers below that limit
    listAbundant = []
    
    for k in range(limit):
        if divisorSum(k+1) > k+1:
            listAbundant.append(k+1)
    
    canAbundant = [False]*(limit+1)
    
    #With this list, we then iterate over the list of abundant integers twice, checking the results of all possible sums of abundant numbers, without repeating previous summations
    #We check up until out limit point, and when we calculate a sum, we know that number can be written as a sum of two abundant numbers, wo we mark it with a boolean to show that it's possible.
    
    for i in range(len(listAbundant)):
        for j in range(i,len(listAbundant)):
            sumA = listAbundant[i] + listAbundant[j]
            if sumA <= limit:# This conditional allows us to break out of the second summation loop if we begin to sum abundant numbers which result in integers over the limit, because we know it's always possible over the limit, therefore no need to check
                canAbundant[sumA] = True
            else:
                break
    
    
    #Now to sum all non-two-abundant-sum numbers
    nonSum = 0
    
    for n in range(len(canAbundant)):
        if not(canAbundant[n]):
            nonSum += n
            
    print(nonSum)