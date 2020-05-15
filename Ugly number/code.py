# -*- coding: utf-8 -*-
"""
Question: Write a program to find the nth ugly number. Ugly numbers are positive numbers
whose prime factors include only 2,3,5

Input = 10, Output = 12

1,2,3,4,5,6,8,9,10,12 

Constraint: 1 is always an ugly number, n does not exceed 1690
"""

import sys
import math
import time

n = input("Enter the nth ugly number to find: ")

#Create a number generator and check for divisibility (mod) and get the quotient
            
## Create function to get prime factors
def find_prime_factors(n):
    #start = time.time()
    
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n = n/2
    
    ##The remaining number must be odd, so check with the odd numbers
    ## 
    for i in range(3, int(math.sqrt(n))+1,2):
        while n % i == 0:
            factors.add(i)
            n = n/i
    if n > 1:
        factors.add(n)   
    #end = time.time()
    #print('Time taken to find all the factors: {}'.format(end-start))    
    return factors

#print(find_prime_factors(1690))

num_list = []
num_list.append(1)
count = 1
num = 2
while count < int(n):
    factor = find_prime_factors(num)
    if len(factor) > 3:
        num += 1
        continue
    else:
        if all(x in [2,3,5] for x in list(factor)):
            count +=1
            num_list.append(num)
        num +=1
        continue
        
print(num_list)
print('{} Ugly number is {}'.format(int(n), num_list[-1]))
    
