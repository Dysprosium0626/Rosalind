#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 17:03
# @Author  : Dysprosium
# @File    : EX001_Counting_DNA_Nucleotides.py


def count_dna(seq):
    print('%d %d %d %d' % (seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')))


f = open("rosalind_dna.txt", 'r')
seq = f.read()