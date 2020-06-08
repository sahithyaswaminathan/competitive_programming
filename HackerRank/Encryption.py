"""
Chapter: Problem Solving - Implementation

Difficulty: Medium

Question Name: Encryption

Question description: 

Complete the encryption function in the editor below. It should return a single string composed as described.

encryption has the following parameter(s):

s: a string to encrypt
Input Format

One line of text, the string 

Constraints: 1 <= |s| <= 81


s is comprised only of characters in the range ascii[a-z].

Output Format

Print the encoded message on one line as described.

Sample Input:
haveaniceday

Sample Output:
hae and via ecy
"""

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ", "")
    L = len(s)
    ##get ideal rows and columns
    rows, cols = ismincondition(L)
    ##Check if rows and cols are not Null
    ##Create two layers dict
    library = {}
    i = 0
    for r in range(rows):
        library[r] = {}
        for c in range(cols):
            if i < len(s):
                library[r][c] = s[i]
                i = i+1
    ##Print the value 
    out = str()
    residue = (rows*cols) - L
    for p1 in range(cols):
        if p1 > 0:
            out = out + " "
        if (p1 < cols - residue) or (residue == 0):
            for p2 in range(rows):
                #if library[p2][p1]:
                out = out+library[p2][p1]
        else:
            for p2 in range(rows-1):
                out = out+library[p2][p1]

    return out

def ismincondition(L):
    """
    Input L - length of string without spaces
    """
    minlimit = math.floor(math.sqrt(L))
    maxlimit = math.ceil(math.sqrt(L))
    for cols in range(minlimit, maxlimit+1):
        for rows in range(minlimit, cols+1):
            if rows*cols >= L:
                break
    return rows,cols
    
    
if __name__ == '__main__':
    """
    As Given in Hackerrank: Please change this as per the IDE
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
