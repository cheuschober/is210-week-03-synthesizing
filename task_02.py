#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

SPANISH = inquisition.SPANISH
I = SPANISH.index('Spanish', 1)
N = len('Spanish')
L = len(SPANISH)
FISHY = SPANISH[0:I] + 'Flemish' + SPANISH[I+N:L]
