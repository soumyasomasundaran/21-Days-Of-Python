"""
This is a module that finds the sum  and product of elements in a list

created on 31 Jan 2021
"""
def sum_list(l):
    s = 0
    for i in l:
        s = s + i
    print(s)


def product_list(l):
    p = 1
    for i in l:
        p = p * i
    print(p)


