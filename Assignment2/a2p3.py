#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2020 <<Insert your name here>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 2 Student Solution
September 2020
Author: Christopher Pontikes
"""
import math
def decryptMessage(key:list, message: str):
    numRows = math.ceil(len(message)/len(key)) #calculate how many rows are required (round up)
    counter = 0
    ciphertext = [["" for i in range(len(key))] for j in range(numRows)] #create the array with correct number of rows and columns

    #highlighting valid places in the array characters can go, accounting for when length of message
    #and length of keyword do not divide evenly
    for i in range(numRows):
        for j in range(len(key)):
            if counter < len(message):
                ciphertext[i][j] = "0"
                counter +=1

    #placing the characters in the highlighted spots and proper columns
    counter1 = 0
    for i in range(len(key)):
        k = key[i]
        for j in range(numRows):
            if ciphertext[j][k-1] == "0":
                ciphertext[j][k-1] = message[counter1]
                counter1+=1

    #putting the whole thing together
    ct = []
    for i in range(numRows):
        for j in range(len(key)):
            ct.append(ciphertext[i][j])

    return "".join(ct)

def test():
    assert decryptMessage([2,4,1,5,3], "IS HAUCREERNP F") == "CIPHERS ARE FUN"


from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
