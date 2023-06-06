# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 17:36:30 2023

@author: kanis
"""

import matplotlib.pyplot as plt

data = [[0,0,0,0,0,0,0,0],
       [0,0,1,1,1,1,0,0],
       [0,0,1,0,0,1,0,0],
       [0,0,1,0,0,1,0,0],
       [0,0,1,0,0,1,0,0],
       [0,0,1,0,0,1,0,0],
       [0,0,1,1,1,1,0,0],
       [0,0,0,0,0,0,0,0]]

plt.imshow(data, cmap = "gray")
plt.show()