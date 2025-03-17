# -*- coding: utf-8 -*-
"""
Created by Preston Seligman
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt
#%% Voltage vs. Photocurrent
#%%%
#Pandas is Insane
df = pd.read_csv("pe_data.csv") #Convert data to pandas dataframe
led1x = df.query("LED == 1")["Voltage"].to_numpy() #Query for LED 1 and save voltage as np.array
led1y = df.query("LED == 1")["Current"].to_numpy() #..
led3x = df.query("LED == 3")["Voltage"].to_numpy()
led3y = df.query("LED == 3")["Current"].to_numpy()
led5x = df.query("LED == 5")["Voltage"].to_numpy()
led5y = df.query("LED == 5")["Current"].to_numpy()
led7x = df.query("LED == 7")["Voltage"].to_numpy()
led7y = df.query("LED == 7")["Current"].to_numpy()
rawerr1 = df.query("LED == 1")["Error"].to_numpy()
rawerr3 = df.query("LED == 3")["Error"].to_numpy()
rawerr5 = df.query("LED == 5")["Error"].to_numpy()
rawerr7 = df.query("LED == 7")["Error"].to_numpy()


#%%% Sepeate Plots
#Plot data for each LED in subplots
fig1 = plt.figure(figsize=(8,8), layout="constrained")
ax = fig1.subplot_mosaic([["led1","led3"],
                          ["led5","led7"]])


#LED 1
ax["led1"].set_title("LED 1")
ax["led1"].hlines(range(0,31,5), xmin=0.5,xmax=2, color="0.8") #Plot grid lines
ax["led1"].vlines(np.linspace(0.5,2.0,num=7),ymin=0,ymax=30, color="0.8")
ax["led1"].plot(led1x, led1y, color="C0")
ax["led1"].set_xlabel("Voltage (V)")
ax["led1"].set_ylabel("Photocurrent (nA)")
ax["led1"].errorbar(led1x, led1y, yerr=rawerr1, fmt="o", capsize=4) #Plot error bars


ax["led3"].set_title("LED 3")
ax["led3"].hlines(range(0,31,5), xmin=0.6,xmax=1.8, color="0.8")
ax["led3"].vlines(np.linspace(0.6,1.8,num=7),ymin=0,ymax=30, color="0.8")
ax["led3"].plot(led3x, led3y, color="C1")
ax["led3"].set_xlabel("Voltage (V)")
ax["led3"].set_ylabel("Photocurrent (nA)")
ax["led3"].errorbar(led3x, led3y, yerr=rawerr3, fmt="o", capsize=4, color="C1")


ax["led5"].set_title("LED 5")
ax["led5"].hlines(range(0,31,5), xmin=0.6,xmax=1.6, color="0.8")
ax["led5"].vlines(np.linspace(0.6,1.6,num=6),ymin=0,ymax=30, color="0.8")
ax["led5"].plot(led5x, led5y, color="C2")
ax["led5"].set_xlabel("Voltage (V)")
ax["led5"].set_ylabel("Photocurrent (nA)")
ax["led5"].errorbar(led5x, led5y, yerr=rawerr5, fmt="o", capsize=4, color="C2")

ax["led7"].set_title("LED 7")
ax["led7"].hlines(range(0,31,5), xmin=0.4,xmax=1.2, color="0.8")
ax["led7"].vlines(np.linspace(0.4,1.2,num=5),ymin=0,ymax=30, color="0.8")
ax["led7"].plot(led7x, led7y, color="C3")
ax["led7"].set_xlabel("Voltage (V)")
ax["led7"].set_ylabel("Photocurrent (nA)")
ax["led7"].errorbar(led7x, led7y, yerr=rawerr7, fmt="o", capsize=4, color="C3")

plt.show()

#%%% Single Plot
#Plot data for LEDs on one plot, must comment out other plot
plt.plot(led1x, led1y, color="C0", label=r"LED 1, Freq $7.13*10^{14}$ Hz")
plt.plot(led3x,led3y,color="C1", label=r"LED 3, Freq $6.81*10^{14}$ Hz")
plt.plot(led5x,led5y,color="C2", label=r"LED 5, Freq $6.52*10^{14}$ Hz")
plt.plot(led7x,led7y,color="C3", label=r"LED 7, Freq $5.88*10^{14}$ Hz")
plt.errorbar(led1x,led1y,yerr=rawerr1,fmt=".",capsize=5,color="purple")
plt.errorbar(led3x,led3y,yerr=rawerr3,fmt=".",capsize=5,color="purple")
plt.errorbar(led5x,led5y,yerr=rawerr5,fmt=".",capsize=5,color="purple")
plt.errorbar(led7x,led7y,yerr=rawerr7,fmt=".",capsize=5,color="purple")
plt.xlabel("Voltage (V)")
plt.ylabel("Photocurrent (nA)")
plt.title("Voltage vs Photocurrent")
plt.legend(loc="upper right")
plt.hlines(range(0,31,5), 0, 2, color="0.8")
plt.vlines(np.linspace(0, 2, num=8), 0, 30, color='0.8')
plt.show()
#%% Frequency vs. Stopping Voltage
xdata, ydata, yerror = np.loadtxt("freq_vs_stopping.txt", unpack=True) #Load data


def func(x,s,b):
    return s*x+b




parameters, covariance = opt.curve_fit(func, xdata, ydata,sigma = yerror)


#Error on the fits
perr = np.sqrt(np.diag(covariance))

print(f"s={parameters[0]}, b={parameters[1]}") #Print fits
print(f"Error: s={perr[0]}, b={perr[1]}") #Print fitting errors

plt.plot(xdata,func(xdata,*parameters),label = 'Linear Fit', color="orange")
plt.errorbar(xdata,ydata,yerr=yerror,capsize = 5,marker = 'o',color="blue",linestyle = 'None', label = 'LED Frequency')
plt.xlabel("LED Frequency (Hz)")
plt.xlim(5.8e14,7.2e14)
plt.ylabel("Stopping Voltage (V)")
plt.title("Frequency vs. Stopping Voltage")
plt.legend(loc="upper left")