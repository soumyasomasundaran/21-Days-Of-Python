"""
This is a module that calculates the sum and product of a list of numbers

Created on Jan 23 2021
"""

quote = "There should be no such thing as boring mathematics."


def sum_n(l):
    sum = 0
    for i in l:
        sum = sum + i
    print(sum)


def product_n(l):
    product = 1
    for i in l:
        product = product * i
    print(product)


