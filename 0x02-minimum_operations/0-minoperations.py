#!/usr/bin/python3
'''
Calculates the fewest number of operations needed to result in
exactly n H characters in the file.
'''

import math


def numb_factors(n):
    ''' Factors of the number n '''
    list = []
    while n % 2 == 0:
        list.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            list.append(i)
            n = n / i
    if n > 2:
        list.append(n)
    return list


def minOperations(n):
    ''' Return an integer, if n is impossible to achieve, return 0 '''
    if type(n) != int or n < 2:
        return 0
    else:
        operations = sum(numb_factors(n))
        return int(operations)
