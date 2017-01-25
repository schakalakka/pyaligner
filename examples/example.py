#!/usr/bin/env python

__autor__ = 'Andreas Radke'
__copyright__ = 'Copyright 2017, '
__license__ = 'GPL'
__version__ = '0.1'

from src import alignment, overlap

########################################################
# example 1
# Output:
# Score: -1
# ---cgtact-c
#    || | | |
# gatcgca-tgc
print('Example 1')
alignment.align('cgtactc', 'gatcgcatgc', print_alignment=True)

########################################################
# example 2
# Output:
# Score: 10
# Thomas M-üller
# ||||||||  ||||
# Thomas Mueller
print('\nExample 2')
alignment.align('Thomas Müller', 'Thomas Mueller', print_alignment=True)

########################################################
# example 3
# Output:
# Score: 9
# Thomas M-üller
# ||||||||  ||||
# Thomas Mueller
gap_open = -2
print('\nExample 3')
alignment.align('Thomas Müller', 'Thomas Mueller', print_alignment=True, gap_open=gap_open)

########################################################
# example 4
# Output:
# Score: 2
# aaabbb---
#     ||
# ----bbaaa
print('\nExample 4')
overlap.overlap('aaabbb', 'bbaaa', print_alignment=True)

########################################################
# example 5
# Output:
# Score: 3
# bbaaa---
#   |||
# --aaabbb
print('\nExample 5')
overlap.overlap('bbaaa', 'aaabbb', print_alignment=True)

########################################################
# example 6
# Output:
# Score: 3
# bbaaa---
#   |||
# --aaabbb
print('\nExample 6')
overlap.naive_overlap('bbaaa', 'aaabbb', print_alignment=True)
