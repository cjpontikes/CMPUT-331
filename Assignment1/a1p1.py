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
CMPUT 331 Assignment 1 Student Solution
September 2020
Author: Christopher Pontikes 1499276
"""
validLetters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

def encrypt(message: str, key: str):

    translated = ''
    shift = validLetters.find(key) #determines how much to shift the message letters by

    #for loops goes through each character to determine if it is a valid letter
    #or not, then will encrypt it if it is a valid letter
    for character in message:
        if character in validLetters:
            num = validLetters.find(character)+shift #adds the key amount for shift

            #the following if else tree was copied from ceaserCipher.py
            if num >= len(validLetters):
              num = num - len(validLetters)
            elif num < 0:
              num = num + len(validLetters)

            translated = translated + validLetters[num] #adds the new encrypted character to the string
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + character

    return str(translated)

def decrypt(message: str, key: str):

    translated = ''
    shift = validLetters.find(key)

    #for loops goes through each character to determine if it is a valid letter
    #or not, then will decrypt it if it is a valid letter
    for character in message:
        if character in validLetters:
            num = validLetters.find(character)-shift #subtracts the key amount for shift

            #the following if else tree was copied from ceaserCipher.py
            if num >= len(validLetters):
              num = num - len(validLetters)
            elif num < 0:
              num = num + len(validLetters)

            translated = translated + validLetters[num]
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + character

    return str(translated)


def test():
    assert decrypt(encrypt("foo", "g"), "g") == "foo"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
