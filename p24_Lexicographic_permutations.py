# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:54:55 2022

@author: willi
"""

#Project Euler Problem 24 Lexicographic permutations


#There are 10! factorial permutations of digits 0 through 9. Which is 3628800 possibilities. Sort of inefficient to make a full array?
#Using itertools permutation function computes all permutations in O(n*n!) time for the n! permutations and O(n) time to genarate a permutation
#More efficient to write the equivalent permutation finding function which includes lexicographical ordering and perform generation one million -1 times.
#This yields O(n) time to produce a permutation still.

#This code is influenced by the following blog post "https://www.geeksforgeeks.org/lexicographic-permutations-of-string/"

def findFirst(string): #Returns None if string is in non-increasing order
    #Finds rightmost character which is smaller than the next character in the string. Uses Python reverse indexing with negative numbers
    for j in range(2,len(string)+1):#Starts with second to last character in rightmost search
        if string[-j] < string[-j+1]:
            return len(string)-j #Returns index of character
    return None
    
def findSecond(string,firstIndex):
    
    if firstIndex == None:
        raise Exception("First Index is None, meaning string is in non-increasing order, therefore no more permutations to compute")
    
    if firstIndex >= len(string)-1:
        raise Exception("First Character Index outside string bounds. String: {}; String Length: {}; firstIndex: {}".format(string,len(string),firstIndex))
    
    ceil = string[firstIndex+1] #Must initialize a starting character that we know is greater than the first character in order to comute cieling, will change ceiling is smaller character is found
    secondIndex = firstIndex+1
    #But by definition of the first character, the character to the right of it in the string is greater than the first character.
    for i in range(firstIndex+1,len(string)):
        if string[i] < ceil and string[i] > string[firstIndex]:
            ceil = string[i]
            secondIndex = i
    return secondIndex

def computeNextLexPerm(string):
    firstIndex = findFirst(string)
    if firstIndex == None:
        print("No Lexicographically lower permutation.")
        return None
    secondIndex = findSecond(string, firstIndex)
    
    string = swapChar(string,firstIndex,secondIndex)
    left = string[:firstIndex+1]
    right = string[firstIndex+1:][::-1]
    string = left + right
    return string

def swapChar(string,i,j):
    #can intake any order, but my convention we make i the rightmost character
    if i > j:
        temp = j
        j = i
        i = temp
    if i == j:#Swap with itself. No change
        return string
    
    left = string[:i]
    charI = string[i]
    mid = string[i+1:j]
    charJ = string[j]
    right = string[j+1:]
    
    string = left + charJ + mid + charI + right
    return string

if __name__=="__main__":
    
    string = "0123456789"
    
    lastPerm = 1000000
    
    print(string) 
    for i in range(lastPerm-1):
        string = computeNextLexPerm(string)
        #print(string)
    print(string)
    