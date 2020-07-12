#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 12:15
# @Author  : Dysprosium
# @File    : EX003_Complementing_a_Strand_of_DNA.py


def reverse_chain(seq):
    seq_rev = seq[::-1]
    seq_dna_rev = ''
    for i in seq_rev:
        if i == 'A':
            seq_dna_rev += 'T'
        elif i == 'C':
            seq_dna_rev += 'G'
        elif i == 'G':
            seq_dna_rev += 'C'
        elif i == 'T':
            seq_dna_rev += 'A'
    print(seq_dna_rev)


f = open('rosalind_revc.txt', 'r')
seq = f.read()

