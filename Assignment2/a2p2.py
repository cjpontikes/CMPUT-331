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
Author: Christopher Pontikes 1499276
"""
import math

def encryptMessage(key:list, message: str):
    numRows = math.ceil(len(message)/len(key)) #calculate how many rows are required (round up)
    counter = 0
    ciphertext = [["" for i in range(len(key))] for j in range(numRows)] #create the array with correct number of rows and columns

    #placing the characters into the array, stopping when the end of the message is reached
    for i in range(numRows):
        for j in range(len(key)):
            if counter < len(message):
                ciphertext[i][j] = message[counter]
                counter+=1


    ct = []
    for i in range(len(key)):
        #determine which column is added first
        k = key[i]
        #adding the correct column first
        for j in range(numRows):
            ct.append(ciphertext[j][k-1])

    return "".join(ct)

def test():
    assert encryptMessage([2,4,1,5,3], "CIPHERS ARE FUN") == "IS HAUCREERNP F"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
