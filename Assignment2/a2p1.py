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

def encryptMessage(key:int, message: str):
    ciphertext = [["" for i in range(len(message))] for j in range(key)]

    row = 0
    flag = 0

    for i in range(len(message)):
        ciphertext[row][i] = message[i]

        if flag==0:
            row+=1
            if row==key-1:
                flag = 1
        else:
            row-=1
            if row==0:
                flag = 0

    ct = []
    for i in range(key):
        for j in range(len(message)):
            ct.append(ciphertext[i][j])

    return "".join(ct)

def decryptMessage(key:int, message: str):
    ciphertext = [["" for i in range(len(message))] for j in range(key)]
    row = 0
    flag = 0
    counter = 1
    ciphertext[0][0] = message[0]
    for i in range(len(ciphertext)):
        for j in range(1,len(message)):
            if flag==0:
                row+=1
                if row==key-1:
                    flag = 1
            else:
                row-=1
                if row==0:
                    flag = 0
            if row == i:
                ciphertext[row][j] = message[counter]
                counter+=1

    ct = []
    flag1 = 0
    row1 = 0
    for i in range(len(message)):
        ct.append(ciphertext[row1][i])
        if flag1==0:
            row1+=1
            if row1==key-1:
                flag1 = 1
        else:
            row1-=1
            if row1==0:
                flag1 = 0

    return "".join(ct)

def test():
    assert decryptMessage(3, encryptMessage(3, "CIPHERS ARE FUN")) == "CIPHERS ARE FUN"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
