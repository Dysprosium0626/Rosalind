#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 12:59
# @Author  : Dysprosium
# @File    : EX004_Rabbits_and_Recurrence_Relations.py

f = open('rosalind_fib.txt', 'r')
numbers = f.read().split()


def fibonacci(months, k):
    if months == 1 or months == 2:
        return 1
    else:
        return fibonacci(months-2, k) * k + fibonacci(months-1, k)


print(fibonacci(int(numbers[0]), int(numbers[1])))