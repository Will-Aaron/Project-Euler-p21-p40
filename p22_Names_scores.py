# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:23:59 2022

@author: willi
"""

#Project Euler Problem 22



def alphaValue(string):
    #By convention all letters in text file are capitalized, and by using the ord method, we can find the ascii value of the character, then convert the ascii value to it's order in the alphabet.
    #"A" has an ascii value of 65, so to convert that number to 1 as the first letter of the alphabet, simply subtract by 64 and do so for all other characters
    alphaVal = 0
    for char in string:
        alphaVal += ord(char)-64
    return alphaVal
    

if __name__=="__main__":
    with open('p022_names.txt','r') as file:
        text = file.read().replace('\n',',').replace("\"",'')
    
    namesList = text.split(",")#Using python's built-in TimSort is more efficient than anything else
    
    namesList.sort()
    
    totalNameScore = 0
    
    for i in range(len(namesList)):
        totalNameScore += alphaValue(namesList[i]) * (i+1)
    
    print(totalNameScore)