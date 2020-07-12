#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 12:05
# @Author  : Dysprosium
# @File    : EX002_Transcribing_DNA_into_RNA.py


def dna_to_rna(seq):
    print(seq.replace('T', 'U'))


f = open('rosalind_rna.txt', 'r')
seq = f.read()