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
from a2p3 import decryptMessage #importing the decryptMessage function

#function to open a file and read its contents
def readFile(filename: str):
    file = open(filename, encoding="utf8")
    message = file.read()
    file.close()
    return message

#function to create a new file and write to it
def uploadFile(filename:str, message: str):
    file = open(filename, 'w+')
    file.write(message)
    file.close()

#function that combines the other two while also running the decryptMessage function
def decryptMystery():
    uploadFile("mystery.dec.txt", decryptMessage([8,1,6,2,10,4,5,3,7,9], readFile("mystery.txt")))

if __name__ == "__main__":
    decryptMystery()
