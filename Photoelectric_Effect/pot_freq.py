# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 22:52:26 2025

@author: golfp
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


xdata, ydata, yerror = np.loadtxt("freq_pot.txt", unpack=True)


def func(x,s,b):
    return s*x+b




parameters, covariance = opt.curve_fit(func, xdata, ydata,sigma = yerror)


#Error on the fits
perr = np.sqrt(np.diag(covariance))

print(f"s={parameters[0]}, b={parameters[1]}")
print(f"Error: s={perr[0]}, b={perr[1]}")

plt.plot(xdata,func(xdata,*parameters),label = 'Linear Fit', color="orange")
plt.errorbar(xdata,ydata,yerr=yerror,capsize = 5,marker = 'o',color="blue",linestyle = 'None', label = 'LED Frequency')
plt.xlabel("LED Frequency (Hz)")
plt.xlim(5.8e14,7.2e14)
plt.ylabel("Stopping Voltage (V)")
plt.title("Frequency vs. Stopping Voltage")
plt.legend(loc="upper left")

