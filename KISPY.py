# -*- coding: utf-8 -*-
"""Untitled43.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19eb5NBldXfaguNQL0VCdCYK4R0hNygxX
"""

import numpy as np
import matplotlib.pyplot as plt
import random

logo = np.full((30,49,3), 255, dtype="uint8")

black = [(8, 20), (8, 21), (8, 22), (8, 23), (8, 24), (8, 25), (7, 30), (8, 16), (7, 19), (7, 26), (6, 30), (7, 16), (6, 18), (6, 27), (5, 16), (5, 17), (5, 28), (5, 29), (6, 16) ,(8, 30),(9, 15),(9, 30),(10, 15) ,(11, 15),(10, 30),(12, 15),(11, 31),(12, 20),(12, 28),(12, 31),(13, 15),(13, 20),(13, 19),(13, 25),(13, 28),(13, 27),(14, 15),(13, 31),(14, 31),(15, 15),(15, 20),(15, 24),(15, 27),(15, 31),(16, 16),(16, 20), (16, 21), (16, 22), (16, 23), (16, 24), (16, 25), (16, 26), (16, 27),(16, 30),(17, 17),(17, 29), (18, 18), (18, 19), (18, 20), (18, 21), (18, 22), (18, 23), (18, 24), (18, 25), (18, 26), (18, 27), (18, 28), (21, 2), (21, 5), (21, 7), (21, 8), (21, 9), (21, 12), (21, 13), (21, 14), (21, 16), (21, 17), (21, 18), (21, 21), (21, 25), (21, 27), (21, 28), (21, 29), (21, 30), (21, 31), (21, 33), (21, 36), (21, 39), (21, 40), (21, 43), (21, 46), (22, 2), (22, 4), (22, 8), (22, 11), (22, 16), (22, 19), (22, 21), (22, 25), (22, 29), (22, 33), (22, 36), (22, 38), (22, 41), (22, 43), (22, 44), (22, 46), (23, 2), (23, 3), (23, 8), (23, 12), (23, 13), (23, 16), (23, 17), (23, 18), (23, 22), (23, 23), (23, 24), (23, 29), (23, 33), (23, 34), (23, 35), (23, 36), (23, 38), (23, 41), (23, 43), (23, 45), (23, 46), (24, 2), (24, 4), (24, 8), (24, 14), (24, 16), (24, 23), (24, 29), (24, 33), (24, 36), (24, 38), (24, 41), (24, 43), (24, 46), (25, 2), (25, 5), (25, 7), (25, 8), (25, 9), (25, 11), (25, 12), (25, 13), (25, 16), (25, 23), (25, 29), (25, 33), (25, 36), (25, 39), (25, 40), (25, 43), (25, 46) ]
gray = [(6, 17), (6, 28), (6, 29), (7, 17), (7, 18), (7, 27), (7, 28), (7, 29), (8, 17), (8, 18), (8, 19), (8, 26), (8, 27), (8, 28), (8, 29), (9, 16), (9, 17), (9, 18), (9, 19), (9, 20), (9, 21), (9, 22), (9, 23), (9, 24), (9, 25), (9, 26), (9, 27), (9, 28), (9, 29) ,(10, 16), (10, 17), (10, 18), (10, 19), (10, 20), (10, 21), (10, 22), (10, 23), (10, 24), (10, 25), (10, 26), (10, 27), (10, 28), (10, 29) ,(11, 16), (11, 17), (11, 18), (11, 19), (11, 20), (11, 21), (11, 22), (11, 23), (11, 24), (11, 25), (11, 26), (11, 27), (11, 28), (11, 29), (11, 30) ,(12, 18),(12, 17),(12, 16),(12, 21), (12, 22), (12, 23), (12, 24), (12, 25), (12, 26) ,(12, 29),(12, 30),(13, 18),(13, 17),(13, 16),(13, 24) ,(13, 23) ,(13, 22),(13, 21) ,(13, 26),(13, 30),(13, 29),(14, 16),(14, 19), (14, 20), (14, 21), (14, 22), (14, 23), (14, 24), (14, 25), (14, 26), (14, 27), (14, 28), (15, 16),(15, 19),(15, 23),(15, 22),(15, 21),(15, 25),(15, 26),(15, 28),(16, 19),(16, 18),(16, 17),(16, 28) ,(16, 29),(17, 18), (17, 19), (17, 20), (17, 21), (17, 22), (17, 23), (17, 24), (17, 25), (17, 26), (17, 27), (17, 28) ]
pink = [(14, 17),(14, 18),(14, 30),(14, 29),(15, 17),(15, 18),(15, 30),(15, 29)]

for i,j in black:
    logo[i,j] = [0, 0, 0]
for i,j in gray:
    logo[i,j] = [200, 200, 200]
for i,j in pink:
    logo[i,j] = [255, 205, 210]

plt.imshow(logo)