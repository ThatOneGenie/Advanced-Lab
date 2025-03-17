# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 20:57:10 2025

@author: golfp
"""

import numpy as np
import matplotlib.pyplot as plt
#%%
xdata, current, ydata, yerror = np.loadtxt("peak.txt", unpack=True)
plt.errorbar(xdata,ydata,yerr=yerror,capsize = 5,marker = 'o',linestyle = 'None', label = 'Frequency')
plt.xlabel("Laser")
plt.ylabel("Frequency")
plt.legend(loc="upper left")
plt.xticks(ticks=xdata)
plt.title("Laser Frequencies")

plt.show()

#%%
"""
fxdata = 





fig = plt.figure()
axs = fig.subplot_mosaic([["Laser1", "Laser3"],
                          ["Laser5", "Laser7"]])
"""

