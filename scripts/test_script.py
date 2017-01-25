#!/usr/bin/env python

from src import alignment, overlap

__autor__ = 'Andreas Radke'
__copyright__ = 'Copyright 2017, '
__license__ = 'GPL'
__version__ = '0.1'

alignment.align('aab', 'aba', print_alignment=True)

overlap.overlap('aabbba', 'bbb', print_alignment=True)
overlap.overlap('', 'ab', print_alignment=True)
overlap.overlap('bbbaaaaa', 'aaaabbb', print_alignment=True)
alignment.align_score('aab', 'aba', print_alignment=True)
